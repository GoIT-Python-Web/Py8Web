from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from simple.auth import Hash, create_access_token, get_current_user
from simple.db import User, get_db

app = FastAPI()
hash_handler = Hash()


class UserModel(BaseModel):
    email: EmailStr
    password: str


@app.post("/signup")
async def signup(body: UserModel, db: Session = Depends(get_db)):
    exist_user: User | None = db.query(User).filter_by(email=body.email).first()
    if exist_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")
    new_user = User(email=body.email, password=hash_handler.get_password_hash(body.password))
    db.add(new_user)
    db.commit()
    return {"id": new_user.id, "email": new_user.email}


@app.post("/login")
async def signup(body: UserModel, db: Session = Depends(get_db)):
    user: User | None = db.query(User).filter_by(email=body.email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email")
    if not hash_handler.verify_password(body.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    access_token = await create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/secret")
async def secret(current_user: User = Depends(get_current_user)):
    return {"message": f"Secrete router: access for {current_user.email}"}
