from datetime import timedelta
from os import access

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from blog.database import get_db
from blog.hashing import HashPassword
from blog.models import User
from blog.schemas import Login
from blog.token import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token

router = APIRouter(tags=["Auth"], prefix="/api/v1/auth")


@router.post("/login")
async def login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == request.username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    if not HashPassword.verify(request.password, user.password):  # type: ignore
        raise HTTPException(status_code=404, detail="Username or Password is incorrect")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
