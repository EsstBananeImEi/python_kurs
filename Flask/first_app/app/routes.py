from app import app


@app.route("/")
@app.route("/index")
def index():
    return "Hello, World!"


@app.route("/user")
def user():
    return f"<h1>Hello Sebastian</h1>"
