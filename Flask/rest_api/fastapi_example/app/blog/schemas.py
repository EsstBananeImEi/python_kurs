from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class User(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config:
        from_attributes = True


class ShowUser(BaseModel):
    email: str
    first_name: str
    last_name: str
    blogs: list[Blog] = []

    class Config:
        from_attributes = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:
        from_attributes = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
