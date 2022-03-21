from app import db, init_app
from app.models import Post, User, Notification

app = init_app()


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post, "Notification": Notification}
