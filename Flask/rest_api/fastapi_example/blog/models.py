
from sqlalchemy import Column, DateTime, Integer, String, literal

from .database import Base


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    body = Column(String(500))
    published = Column(DateTime)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(120))
    password = Column(String(120))
