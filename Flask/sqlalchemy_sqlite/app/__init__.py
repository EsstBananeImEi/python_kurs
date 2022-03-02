import logging
import os
from logging.handlers import RotatingFileHandler

from config import Config
from flask import Flask, request
from flask_babel import Babel
from flask_babel import lazy_gettext as _l
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app: Flask = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "login"  # type: ignore Type cannot be assigned to type "None"
login.login_message = _l("Please log in to access this page.")  # type: ignore
mail = Mail(app)
moment = Moment(app)
babel = Babel(app)

from app.auth import auth_blueprint
from app.errors import error_blueprint
from app.main import main_blueprint

app.register_blueprint(error_blueprint)

app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(main_blueprint)


if not app.debug:
    if not os.path.exists("logs"):
        os.mkdir("logs")
    file_handler = RotatingFileHandler(
        "logs/flask_blog.log", maxBytes=10240, backupCount=10
    )
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
        )
    )
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info("Blog startup")


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config["LANGUAGES"])
