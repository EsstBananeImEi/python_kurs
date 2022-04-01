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

class Blog(BaseModel):
    title: str
    body: str
    
class ShowBlog(BaseModel):
    title: str
    body: str

    class Config():
        orm_mode = True
