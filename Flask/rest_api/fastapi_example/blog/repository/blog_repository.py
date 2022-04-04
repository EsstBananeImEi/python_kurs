from datetime import datetime

from blog.database import write_in_db
from blog.models import Blog
from blog.schemas import Blog as BlogSchema
from fastapi import HTTPException
from sqlalchemy.orm import Session

""" Show all blogs """


def get_all(db: Session):
    return db.query(Blog).all()


""" Show specific blog """


def show(db: Session, blog_id: int):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if blog is None:
        raise HTTPException(status_code=404, detail=f"Blog with {blog_id} not exists")
    return blog


""" Create new blog """


def create(db: Session, request: Blog | BlogSchema):
    blog = write_in_db(
        Blog,
        db,
        **{
            "title": request.title,
            "body": request.body,
            "published": datetime.utcnow(),
            "user_id": 1,
        },
    )
    if blog is None:
        raise HTTPException(status_code=400, detail="Blog not created")
    return blog


""" Delete specific blog """


def delete(db: Session, blog_id: int):
    blog = db.query(Blog).filter(Blog.id == blog_id)

    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with {blog_id} not exists")

    blog.delete(synchronize_session=False)  # type: ignore
    db.commit()
    return "done"


""" Update specific blog """


def update(db: Session, blog_id: int, request: Blog | BlogSchema):
    blog = db.query(Blog).filter(Blog.id == blog_id)

    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with {blog_id} not exists")

    blog.update(request.dict())  # type: ignore
    db.commit()
    return "updated"
