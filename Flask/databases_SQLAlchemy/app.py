from datetime import datetime

from flask import Flask, flash, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_database.db"
app.config["SECRET_KEY"] = "$3cr37K3y"


class NameForm(FlaskForm):
    name: StringField = StringField("Wie ist dein name", validators=[DataRequired()])
    submit: SubmitField = SubmitField("Submit")


@app.route("/")
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


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500


@app.route("/name", methods=["GET", "POST"])
def name_form() -> str:
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("Formular Erfolgreich Versendet")

    return render_template("name.html", name=name, form=form)
