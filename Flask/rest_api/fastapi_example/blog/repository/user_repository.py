from datetime import datetime

from blog.database import write_in_db
from blog.hashing import HashPassword
from blog.models import User
from blog.schemas import User as UserSchema
from fastapi import HTTPException
from sqlalchemy.orm import Session

""" Get specific user """
def show(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


""" Create new user """
def create(db: Session, request: UserSchema):
    hashed_password = HashPassword.bcrypt_hash_password(request.password)
    new_user = write_in_db(
        User,
        db,
        **{
            "email": request.email,
            "first_name": request.first_name,
            "last_name": request.last_name,
            "password": hashed_password,
        },
    )
    if new_user is None:
        raise HTTPException(status_code=400, detail="User not created")
    return new_user
