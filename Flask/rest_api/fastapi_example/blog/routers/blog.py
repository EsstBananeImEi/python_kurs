from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy.orm import Session

from blog.database import get_db, write_in_db
from blog.models import Blog as BlogModel
from blog.schemas import Blog as BlogSchema
from blog.schemas import ShowBlog

""" Initialize the router """
router = APIRouter()


@router.get(
    "/api/v1/blog",
    status_code=status.HTTP_200_OK,
    response_model=list[ShowBlog],
    tags=["Blogs"],
)
async def fetch_blogs(db: Session = Depends(get_db), limit=5):
    blogs = db.query(BlogModel).order_by(BlogModel.id).all()[: int(limit)]
    return blogs


@router.get(
    "/api/v1/blog/{blog_id}",
    status_code=status.HTTP_200_OK,
    response_model=ShowBlog,
    tags=["Blogs"],
)
async def fetch_blog(blog_id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()
    if blog is None:
        raise HTTPException(status_code=404, detail=f"Blog with {blog_id} not exists")
    return blog


@router.post("/api/v1/blog", status_code=status.HTTP_201_CREATED, tags=["Blogs"])
async def create_blog(
    request: BlogSchema, response: Response, db: Session = Depends(get_db)
):
    blog = write_in_db(
        BlogModel,
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


@router.put(
    "/api/v1/blog/{blog_id}", status_code=status.HTTP_202_ACCEPTED, tags=["Blogs"]
)
async def update_blog(blog_id: int, request: BlogSchema, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == blog_id)

    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with {blog_id} not exists")

    blog.update(request.dict())  # type: ignore
    db.commit()
    return "updated"


@router.delete(
    "/api/v1/blog/{blog_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Blogs"]
)
async def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == blog_id)

    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with {blog_id} not exists")

    blog.delete(synchronize_session=False)  # type: ignore
    db.commit()
    return "done"


@router.get("/api/v1/blog/{blog_id}/comments", tags=["Blogs"])
async def fetch_blog_comments(blog_id: int, limit=5):
    return {"data": f"{limit} comments for blog with {blog_id}"}
