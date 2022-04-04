from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from blog.database import get_db
from blog.hashing import HashPassword
from blog.models import User
from blog.schemas import Login

router = APIRouter(tags=["Auth"], prefix="/api/v1/auth")


@router.post("/login")
async def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    if not HashPassword.verify(request.password, user.password):
        raise HTTPException(status_code=404, detail="Username or Password is incorrect")

    return user
