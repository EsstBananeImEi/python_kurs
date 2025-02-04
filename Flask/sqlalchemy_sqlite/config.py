import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    if os.environ.get("FLASK_ENV") == "development":
        os.environ["FLASK_URL"] = "http://localhost:5000"
    SECRET_KEY = os.urandom(24).hex()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
    POSTS_PER_PAGE = 36
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    LANGUAGES = ["en", "de"]
    ELASTICSEARCH_URL = os.environ.get("ELASTICSEARCH_URL") or "http://localhost:9200"
