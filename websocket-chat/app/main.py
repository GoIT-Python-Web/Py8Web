from datetime import datetime, timedelta
from typing import List

from fastapi import FastAPI, Response, Request, Cookie, Form, status, Depends, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.core.config import settings, BASE_DIR
from app.database import get_db
from app.models import User, Message

templates = Jinja2Templates(directory=BASE_DIR / "templates")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.mount("/static", StaticFiles(directory=BASE_DIR / "templates" / "static"))

    @_app.get("/", response_class=HTMLResponse)
    async def root(request: Request, my_session: str | None = Cookie(default=None)):
        auth = my_session
        print(auth)
        return templates.TemplateResponse("pages/index.html", {
            "request": request,
            "title": "The Best Chat",
            "auth": auth
        })

    @_app.get("/chat", response_class=HTMLResponse)
    async def root(request: Request, my_session: str | None = Cookie(default=None), db: Session = Depends(get_db)):
        if my_session:
            messages = db.query(Message).select_from(Message).join(User).limit(30).all()
            return templates.TemplateResponse("pages/chat.html", {
                "request": request,
                "title": "The Best Chat",
                "auth": my_session,
                "messages": messages
            })
        return RedirectResponse(request.base_url, status_code=status.HTTP_303_SEE_OTHER)

    @_app.get("/signin", response_class=HTMLResponse)
    async def root(request: Request):
        return templates.TemplateResponse("pages/signin.html", {
            "request": request,
            "title": "The Best Chat",
            "auth": None
        })

    @_app.post("/signin", response_class=HTMLResponse)
    async def root(request: Request, login: str = Form(), password: str = Form(), db: Session = Depends(get_db)):
        user = User(login=login, password=get_password_hash(password))  # noqa
        db.add(user)
        db.commit()
        return templates.TemplateResponse("pages/login.html", {
            "request": request,
            "title": "The Best Chat",
            "auth": None
        })

    @_app.get("/login", response_class=HTMLResponse)
    async def root(request: Request):
        return templates.TemplateResponse("pages/login.html", {
            "request": request,
            "title": "The Best Chat",
            "auth": None
        })

    @_app.post("/login", response_class=HTMLResponse)
    async def root(request: Request, login: str = Form(), password: str = Form(), db: Session = Depends(get_db)):
        user = db.query(User).filter(User.login == login).first()  # noqa
        if user and verify_password(password, user.password):
            response = RedirectResponse(request.base_url, status_code=status.HTTP_303_SEE_OTHER)
            expires = datetime.utcnow() + timedelta(days=7)
            response.set_cookie(key="my_session", value=f"{user.login}", secure=True, httponly=True,
                                expires=expires.strftime("%a, %d %b %Y %H:%M:%S GMT"))
            return response

        return templates.TemplateResponse("pages/login.html", {
            "request": request,
            "title": "The Best Chat",
            "auth": None
        })

    @_app.get("/signout", response_class=HTMLResponse)
    async def root(request: Request, my_session: str | None = Cookie(default=None)):

        response = RedirectResponse(request.base_url, status_code=status.HTTP_303_SEE_OTHER)
        if my_session:
            expires = datetime.utcnow() + timedelta(days=-1)
            response.set_cookie(key="my_session", value=f"", secure=True, httponly=True,
                                expires=expires.strftime("%a, %d %b %Y %H:%M:%S GMT"))

        return response

    @_app.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket,
                                 my_session: str | None = Cookie(default=None),
                                 db: Session = Depends(get_db)):
        await manager.connect(websocket)  # noqa
        try:
            while True:
                data = await websocket.receive_text()
                user = db.query(User).filter(User.login == my_session).first()  # noqa
                msg = Message(message=data, user_id=user.id)
                db.add(msg)
                db.commit()
                await manager.broadcast(f"{my_session}: {data}")
        except WebSocketDisconnect:
            manager.disconnect(websocket)
            await manager.broadcast(f"Client #{my_session} left the chat")

    return _app


app = get_application()
