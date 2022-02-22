from flask import Flask, render_template

app = Flask(__name__)

"""
Filters:
    upper: Alles Großgeschrieben
    lower: Alles Kleingeschrieben
    capitalize: Erster Buchstabe groß
    safe: erlaubt html von außen
    striptags: entfernt html aus text
"""

@app.route("/")
def index():
    first_name = "John"
    my_html_text = "Das ist mein <strong>HTML</strong> text"
    my_title_text = "Das ist mein HTML text"

    favorit_pizza: list[str] = ["Pepperoni", "Cheese", "Fungi", "Salami", "Hawai"]
    my_number = 42
    return render_template(
        "index.html",
        first_name=first_name,
        my_html_text=my_html_text,
        my_title_text=my_title_text,
        favorit_pizza=favorit_pizza,
        my_number=my_number,
    )


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)
