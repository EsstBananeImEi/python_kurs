from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog.database import get_db
from blog.repository import user_repository
from blog.schemas import ShowUser
from blog.schemas import User as UserSchema

""" Initialize the router """
router = APIRouter(tags=["User"], prefix="/api/v1/user")


@router.get("/{user_id}", response_model=ShowUser)
def show(user_id: int, db: Session = Depends(get_db)):
    return user_repository.show(db, user_id)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ShowUser,
)
async def create(request: UserSchema, db: Session = Depends(get_db)):
    return user_repository.create(db, request)
