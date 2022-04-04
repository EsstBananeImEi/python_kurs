from fastapi import FastAPI, Request

from . import models
from .database import engine
from .routers import authentication, blog, user

""" Initialize the app """
app = FastAPI()

""" Create database tables """
models.Base.metadata.create_all(engine)

""" Register the routers """
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)


@app.get("/")
def read_root(request: Request):
    return {"text": "FastApi Section"}
