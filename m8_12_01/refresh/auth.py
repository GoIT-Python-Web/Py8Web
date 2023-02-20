from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from refresh.db import User, get_db

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class Hash:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)


async def create_access_token(data: dict, expires_delta: float | None = None):
    to_encode = data.copy()
    iat = datetime.utcnow()
    if expires_delta:
        expire = iat + timedelta(seconds=expires_delta)
    else:
        expire = iat + timedelta(minutes=15)
    to_encode.update({"iat": iat, "exp": expire, "scope": "access_token"})
    encoded_access_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_access_jwt


async def create_refresh_token(data: dict, expires_delta: float | None = None):
    to_encode = data.copy()
    iat = datetime.utcnow()
    if expires_delta:
        expire = iat = datetime.utcnow() + timedelta(seconds=expires_delta)
    else:
        expire = iat = datetime.utcnow() + timedelta(days=7)
    to_encode.update({"iat": iat, "exp": expire, "scope": "refresh_token"})
    encoded_refresh_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_refresh_jwt


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload["scope"] == "access_token":
            email: str = payload.get("sub")
            if email is None:
                raise credentials_exception
        else:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user: User | None = db.query(User).filter(User.email == email).first()

    if user is None:
        raise credentials_exception
    return user


async def get_email_form_refresh_token(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload['scope'] == 'refresh_token':
            email = payload.get('sub', None)
            return email
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid scope for token')
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials')
