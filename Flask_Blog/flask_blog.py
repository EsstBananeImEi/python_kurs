from app import db, init_app
from app.models import Notification, Post, User

if __name__ == "__main__":
    app = init_app()
    app.run()

    @app.shell_context_processor
    def make_shell_context():
        return {"db": db, "User": User, "Post": Post, "Notification": Notification}
