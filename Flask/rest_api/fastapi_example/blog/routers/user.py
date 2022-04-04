from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy.orm import Session

from blog.database import get_db, write_in_db
from blog.hashing import HashPassword
from blog.models import User as UserModel
from blog.schemas import ShowUser
from blog.schemas import User as UserSchema

""" Initialize the router """
router = APIRouter()


@router.get("/api/v1/user/{user_id}", response_model=ShowUser, tags=["Users"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post(
    "/api/v1/user",
    status_code=status.HTTP_201_CREATED,
    response_model=ShowUser,
    tags=["Users"],
)
async def create_user(
    request: UserSchema, response: Response, db: Session = Depends(get_db)
):
    hashed_password = HashPassword.bcrypt_hash_password(request.password)
    new_user = write_in_db(
        UserModel,
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
