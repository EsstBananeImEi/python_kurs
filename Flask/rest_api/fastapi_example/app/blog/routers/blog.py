from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from blog.database import get_db
from blog.oauth2 import get_current_user
from blog.repository import blog_repository
from blog.schemas import Blog, ShowBlog, User

""" Initialize the router """
router = APIRouter(tags=["Blog"], prefix="/api/v1/blog")


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[ShowBlog],
)
async def get_all(
    db: Session = Depends(get_db),
    limit=5,
):
    return blog_repository.get_all(db)[: int(limit)]


@router.get(
    "/{blog_id}",
    status_code=status.HTTP_200_OK,
    response_model=ShowBlog,
)
async def show(
    blog_id: int,
    db: Session = Depends(get_db),
):
    return blog_repository.show(db, blog_id)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(
    request: Blog,
    db: Session = Depends(get_db),
):
    return blog_repository.create(db, request)


@router.put("/{blog_id}", status_code=status.HTTP_202_ACCEPTED)
async def update(
    blog_id: int,
    request: Blog,
    db: Session = Depends(get_db),
):
    return blog_repository.update(db, blog_id, request)


@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    blog_id: int,
    db: Session = Depends(get_db),
):
    return blog_repository.delete(db, blog_id)


@router.get("/{blog_id}/comments")
async def get_comments(blog_id: int, limit=5):
    return {"data": f"{limit} comments for blog with {blog_id}"}
