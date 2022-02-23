from flask import Flask, render_template

blog = Flask(__name__)


@blog.route("/")
def index() -> str:
    return render_template("")
