from flask import flash, redirect, render_template

from app import app
from app.forms import LoginForm, NameForm


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


@app.route("/name", methods=["GET", "POST"])
def name_form() -> str:
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("Formular Erfolgreich Versendet")

    return render_template("name.html", name=name, form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login requested for user {form.username.data}, remember_me={form.remember_me.data}"
        )
        return redirect("/index")
    return render_template("login.html", title="Sign In", form=form)
