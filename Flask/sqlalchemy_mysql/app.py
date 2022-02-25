from datetime import datetime

from flask import Flask, flash, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Column, DateTime, Integer, String
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://python_kurs:1234@localhost/my_users"
app.config["SECRET_KEY"] = "$3cr37K3y"
database = SQLAlchemy(app)


class Users(database.Model):  # type: ignore
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(80), nullable=False, unique=True)
    date_added = Column(DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Name {self.name}>"


class UserForm(FlaskForm):
    name: StringField = StringField("Name", validators=[DataRequired()])
    email: StringField = StringField("Email", validators=[DataRequired()])
    submit: SubmitField = SubmitField("Submit")


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


@app.route("/user/add", methods=["GET", "POST"])
def add_user() -> str:
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            database.session.add(user)
            database.session.commit()
        name = form.name.data
        form.name.data = ""
        form.email.data = ""
        flash("User wurde der Datenbank hinzugefügt")
    users = Users.query.order_by(Users.date_added)
    return render_template("add_user.html", form=form, name=name, users=users)
