from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from refresh.auth import Hash, create_access_token, create_refresh_token, get_current_user, get_email_form_refresh_token
from refresh.db import User, get_db

app = FastAPI()
hash_handler = Hash()
token_schema = HTTPBearer()


class UserModel(BaseModel):
    username: EmailStr
    password: str


@app.post("/signup")
async def signup(body: UserModel, db: Session = Depends(get_db)):
    exist_user: User | None = db.query(User).filter_by(email=body.username).first()
    if exist_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")
    new_user = User(email=body.username, password=hash_handler.get_password_hash(body.password))
    db.add(new_user)
    db.commit()
    return {"id": new_user.id, "email": new_user.email}


@app.post("/login")
async def signup(body: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user: User | None = db.query(User).filter_by(email=body.username).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email")
    if not hash_handler.verify_password(body.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    access_token = await create_access_token(data={"sub": user.email})
    refresh_token = await create_refresh_token(data={"sub": user.email})
    user.refresh_token = refresh_token
    db.commit()
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@app.post("/refresh")
async def refresh(cred: HTTPAuthorizationCredentials = Depends(token_schema), db: Session = Depends(get_db)):
    token = cred.credentials
    email = await get_email_form_refresh_token(token)
    user: User | None = db.query(User).filter_by(email=email).first()
    if user:
        if user.refresh_token != token:
            user.refresh_token = None
            db.commit()
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    access_token = await create_access_token(data={"sub": user.email})
    # Все нижче прибрать, якщо хочемо, щоб через 7 днів користувач ввів логін і пароль
    refresh_token = await create_refresh_token(data={"sub": user.email})
    user.refresh_token = refresh_token
    db.commit()
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/secret")
async def secret(current_user: User = Depends(get_current_user)):
    return {"message": f"Secrete router: access for {current_user.email}"}
