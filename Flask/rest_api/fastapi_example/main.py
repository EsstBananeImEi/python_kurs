from uuid import uuid4

import uvicorn
from fastapi import FastAPI, Request

from models import Gender, Role, User

app = FastAPI()
db: list[User] = [
    User(id=uuid4(), first_name="John", last_name="Doe", gender=Gender.male, roles=[Role.student]), # type: ignore
    User(id=uuid4(), first_name="Hannah", last_name="Stevens", gender=Gender.female, roles=[Role.student, Role.admin]) # type: ignore
]

@app.get("/")
def read_root(request: Request):
    return {"text": "FastApi Section"}

@app.get("/api/v1/users")
async def fetch_users():
    return db
