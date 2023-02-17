from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, func, DateTime
from sqlalchemy.orm import relationship, declarative_base

from app.database import Base, engine


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    login = Column(String(120), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    created_at = Column(DateTime, default=func.now())


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(Text)
    created_at = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    user = relationship("User", backref="messages")


Base.metadata.create_all(bind=engine)
