from app import db, init_app
from app.models import Post, User
from config import Config

app = init_app(Config)


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
