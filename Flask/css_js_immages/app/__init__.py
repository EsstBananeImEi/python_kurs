from config import Config
from flask import Flask

app: Flask = Flask(__name__)
app.config.from_object(Config)

from app import errors, forms, routes
