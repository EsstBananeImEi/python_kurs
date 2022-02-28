from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    first_name = "John"
    my_html_text = "Das ist mein <strong>HTML</strong> text"
    my_title_text = "Das ist mein HTML text"

    favorit_pizza: list[str] = ["Pepperoni", "Cheese", "Fungi", "Salami", "Hawai"]
    my_numbers: list[int] = [1, 2, 3, 4, 5, 6, 7]
    return render_template(
        "index.html",
        first_name=first_name,
        my_html_text=my_html_text,
        my_title_text=my_title_text,
        favorit_pizza=favorit_pizza,
        my_numbers=my_numbers,
    )


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)
