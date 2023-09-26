from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from blog import models
from blog.database import engine
from blog.routers import authentication, blog, user

""" Initialize the app """
app = FastAPI()

""" Create database tables """
models.Base.metadata.create_all(engine)

""" Register the routers """
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)


@app.get("/")
async def docs_redirect():
    return RedirectResponse(url="/docs")
