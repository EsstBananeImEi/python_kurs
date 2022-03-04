import logging
import os
from logging.handlers import RotatingFileHandler, SMTPHandler

from flask import Flask, current_app, request
from flask_babel import Babel
from flask_babel import lazy_gettext as _l
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = "auth.login"  # type: ignore
login.login_message = _l("Please log in to access this page.")  # type: ignore
mail = Mail()
moment = Moment()
babel = Babel()


def init_app(config):
    """Initialize the core application."""
    app: Flask = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    babel.init_app(app)

    with app.app_context():
        from app.admin import admin_blueprint
        from app.auth import auth_blueprint
        from app.errors import error_blueprint
        from app.main import main_blueprint

        app.register_blueprint(admin_blueprint, url_prefix="/admin")
        app.register_blueprint(auth_blueprint, url_prefix="/auth")
        app.register_blueprint(error_blueprint)
        app.register_blueprint(main_blueprint)

        if not app.debug and not app.testing:
            if app.config["MAIL_SERVER"]:
                auth = None
                if app.config["MAIL_USERNAME"] or app.config["MAIL_PASSWORD"]:
                    auth = (app.config["MAIL_USERNAME"], app.config["MAIL_PASSWORD"])
                secure = None
                if app.config["MAIL_USE_TLS"]:
                    secure = ()
                mail_handler = SMTPHandler(
                    mailhost=(app.config["MAIL_SERVER"], app.config["MAIL_PORT"]),
                    fromaddr="no-reply@" + app.config["MAIL_SERVER"],
                    toaddrs=app.config["SENDER_EMAIL"],
                    subject="Flask Blog Failure",
                    credentials=auth,
                    secure=secure,
                )
                mail_handler.setLevel(logging.ERROR)
                app.logger.addHandler(mail_handler)

            if not os.path.exists("logs"):
                os.mkdir("logs")
            file_handler = RotatingFileHandler(
                "logs/flask_blog.log", maxBytes=10240, backupCount=10
            )
            file_handler.setFormatter(
                logging.Formatter(
                    "%(asctime)s %(levelname)s: %(message)s "
                    "[in %(pathname)s:%(lineno)d]"
                )
            )
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

            app.logger.setLevel(logging.INFO)
            app.logger.info("Flask Blog startup")

        return app


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config["LANGUAGES"])


from app import models
