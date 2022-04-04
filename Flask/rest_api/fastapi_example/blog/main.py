from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException, Request, Response, status
from sqlalchemy.orm import Session

from . import models, schemas
from .database import engine, get_db, write_in_db
from .hashing import HashPassword

app = FastAPI()

models.Base.metadata.create_all(engine)


@app.get("/")
def read_root(request: Request):
    return {"text": "FastApi Section"}


@app.post(
    "/api/v1/user",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ShowUser,
    tags=["Users"],
)
async def create_user(
    request: schemas.User, response: Response, db: Session = Depends(get_db)
):
    hashed_password = HashPassword.bcrypt_hash_password(request.password)
    new_user = write_in_db(
        models.User,
        db,
        **{
            "email": request.email,
            "first_name": request.first_name,
            "last_name": request.last_name,
            "password": hashed_password,
        },
    )
    if new_user is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "User not created"}
    return new_user


@app.get("/api/v1/user/{user_id}", response_model=schemas.ShowUser, tags=["Users"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get(
    "/api/v1/blog",
    status_code=status.HTTP_200_OK,
    response_model=list[schemas.ShowBlog],
    tags=["Blogs"],
)
async def fetch_blogs(db: Session = Depends(get_db), limit=5):
    blogs = db.query(models.Blog).order_by(models.Blog.id).all()[: int(limit)]
    return blogs


@app.get(
    "/api/v1/blog/{blog_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowBlog,
    tags=["Blogs"],
)
async def fetch_blog(blog_id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if blog is None:
        raise HTTPException(status_code=404, detail=f"Blog with {blog_id} not exists")
    return blog


@app.get("/api/v1/blog/{blog_id}/comments", tags=["Blogs"])
async def fetch_blog_comments(blog_id: int, limit=5):
    return {"data": f"{limit} comments for blog with {blog_id}"}


@app.delete(
    "/api/v1/blog/{blog_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Blogs"]
)
async def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)

    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with {blog_id} not exists")

    blog.delete(synchronize_session=False)  # type: ignore
    db.commit()
    return "done"


@app.put("/api/v1/blog/{blog_id}", status_code=status.HTTP_202_ACCEPTED, tags=["Blogs"])
async def update_blog(
    blog_id: int, request: schemas.Blog, db: Session = Depends(get_db)
):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)

    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with {blog_id} not exists")

    blog.update(request.dict())  # type: ignore
    db.commit()
    return "updated"


@app.post("/api/v1/blog", status_code=status.HTTP_201_CREATED, tags=["Blogs"])
async def create_blog(
    request: schemas.Blog, response: Response, db: Session = Depends(get_db)
):
    blog = write_in_db(
        models.Blog,
        db,
        **{
            "title": request.title,
            "body": request.body,
            "published": datetime.utcnow(),
            "user_id": 1,
        },
    )
    if blog is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "Blog not created"}
    return blog
