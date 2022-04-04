from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog.database import get_db
from blog.oauth2 import get_current_user
from blog.repository import user_repository
from blog.schemas import ShowUser, User

""" Initialize the router """
router = APIRouter(tags=["User"], prefix="/api/v1/user")


@router.get("/{user_id}", response_model=ShowUser)
def show(
    user_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return user_repository.show(db, user_id)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ShowUser,
)
async def create(request: User, db: Session = Depends(get_db)):
    return user_repository.create(db, request)
