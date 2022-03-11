from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/user")
def user():
    return render_template("user.html")
