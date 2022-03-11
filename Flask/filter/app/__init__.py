from flask import Flask

app = Flask(__name__)

from Flask.filter.app import routes
