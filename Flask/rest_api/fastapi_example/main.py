from typing import Optional
from uuid import UUID, uuid4

import uvicorn
from fastapi import FastAPI, HTTPException, Request

from models import Blog, Gender, Role, User, UserUpdateRequest

app = FastAPI()
db: list[User] = [
    User(id=uuid4(), first_name="John", last_name="Doe", gender=Gender.male, roles=[Role.student]), # type: ignore
    User(id=uuid4(), first_name="a", last_name="Stevens", gender=Gender.female, roles=[Role.student, Role.admin]), # type: ignore
    User(id=uuid4(), first_name="b", last_name="Stevens", gender=Gender.female, roles=[Role.student, Role.admin]), # type: ignore
    User(id=uuid4(), first_name="v", last_name="Stevens", gender=Gender.female, roles=[Role.student, Role.admin]), # type: ignore
    User(id=uuid4(), first_name="d", last_name="Stevens", gender=Gender.female, roles=[Role.student, Role.admin]), # type: ignore
    User(id=uuid4(), first_name="e", last_name="Stevens", gender=Gender.female, roles=[Role.student, Role.admin]), # type: ignore
    User(id=uuid4(), first_name="h", last_name="Stevens", gender=Gender.female, roles=[Role.student, Role.admin]), # type: ignore
    User(id=uuid4(), first_name="u", last_name="Stevens", gender=Gender.female, roles=[Role.student, Role.admin]), # type: ignore
    User(id=uuid4(), first_name="j", last_name="Stevens", gender=Gender.female, roles=[Role.student, Role.admin]), # type: ignore
    User(id=uuid4(), first_name="k", last_name="Stevens", gender=Gender.female, roles=[Role.student, Role.admin]), # type: ignore
    User(id=uuid4(), first_name="c", last_name="Stevens", gender=Gender.female, roles=[Role.student, Role.admin]), # type: ignore
    ]


@app.get("/")
def read_root(request: Request):
    return {"text": "FastApi Section"}

@app.get("/api/v1/users")
async def fetch_users(limit=5, sort: Optional[str] = "asc"):
    reverse = False if sort == "asc" else True
    return sorted(db, key=lambda x: x.first_name, reverse=reverse)[:int(limit)]

@app.post("/api/v1/users")
async def create_user(user: User):
    user.id = uuid4()
    db.append(user)
    return {"status": 200, "message": "User created successfully"}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"status": 200, "message": "User deleted successfully"}
    raise HTTPException(
        status_code=404, 
        detail=f"User with {user_id} not exists"
        )
   
@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, user_update_request: UserUpdateRequest):
    for user in db:
        if user.id != user_id:
            raise HTTPException(
                status_code=404, 
                detail=f"User with {user_id} not exists"
                )
        if user_update_request.first_name is not None:
            user.first_name = user_update_request.first_name
        if user_update_request.last_name is not None:
            user.last_name = user_update_request.last_name
        if user_update_request.middle_name is not None:
            user.middle_name = user_update_request.middle_name
        if user_update_request.roles is not None:
            user.roles = user_update_request.roles
        return

@app.get("/api/v1/blog")
async def fetch_blogs(limit=5, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f"{limit} published blogs"}
    return {'data': f"{limit} unpublished blogs"}

@app.get("/api/v1/blog/{blog_id}")
async def fetch_blog(blog_id: UUID):
    return {'data': f"Blog with {blog_id}"}

@app.get("/api/v1/blog/{blog_id}/comments")
async def fetch_blog_comments(blog_id: UUID, limit=5):
    return {'data': f"{limit} comments for blog with {blog_id}"}

@app.post("/api/v1/blog")
async def create_blog(request: Blog):
    return {'data': f"Blog with {request.title} created"}
