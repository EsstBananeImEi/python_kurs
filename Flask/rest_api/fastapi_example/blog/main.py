from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request, Response, status
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine, get_db, write_in_db

app = FastAPI()

models.Base.metadata.create_all(engine)


@app.get("/")
def read_root(request: Request):
    return {"text": "FastApi Section"}

@app.post("/api/v1/user", status_code=status.HTTP_201_CREATED)
async def create_user(request: schemas.User, response: Response, db : Session = Depends(get_db)):
    new_user = write_in_db(
        models.User, 
        db,
        **{
            "email": request.email,
            "first_name": request.first_name,
            "last_name": request.last_name,
            "password": request.password
        }
        )
    print(new_user)
    if new_user is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "User not created"}
    return new_user


@app.get("/api/v1/blog", status_code=status.HTTP_200_OK, response_model=list[schemas.ShowBlog])
async def fetch_blogs(db : Session = Depends(get_db), limit=5):
    blogs = db.query(models.Blog).order_by(models.Blog.id).all()[:int(limit)]
    return blogs

@app.get("/api/v1/blog/{blog_id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
async def fetch_blog(blog_id: int, response: Response, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if blog is None:
        raise HTTPException(
            status_code=404, 
            detail=f"Blog with {blog_id} not exists"
            )
    return blog

@app.get("/api/v1/blog/{blog_id}/comments")
async def fetch_blog_comments(blog_id: int, limit=5):
    return {'data': f"{limit} comments for blog with {blog_id}"}

@app.delete("/api/v1/blog/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(blog_id: int, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)

    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with {blog_id} not exists")

    blog.delete(synchronize_session=False) # type: ignore
    db.commit()
    return 'done'

@app.put("/api/v1/blog/{blog_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_blog(blog_id: int, request: schemas.Blog, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)

    if not blog.first():
        raise HTTPException(
            status_code=404, 
            detail=f"Blog with {blog_id} not exists"
            )

    blog.update(request.dict()) # type: ignore
    db.commit()
    return "updated"

@app.post("/api/v1/blog", status_code=status.HTTP_201_CREATED)
async def create_blog(request: schemas.Blog, response: Response, db : Session = Depends(get_db)):
    blog = write_in_db(
        models.Blog, 
        db,
        **{
            'title': request.title, 
            'body': request.body, 
            "published": datetime.utcnow()
            }
        )
    if blog is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "Blog not created"}
    return blog
