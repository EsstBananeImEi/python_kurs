from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse

from app import app, db
from app.forms import LoginForm, NameForm, RegistrationForm, UserForm
from app.models import User


@app.route("/")
@app.route("/index")
@login_required
def index():
    posts = [
        {
            "author": {"username": "Daniel"},
            "body": "Ein Wunderschöner Tag auf in Deutschland",
        },
        {"author": {"username": "Susanne"}, "body": "Der neue Avengers war sooo Geil!"},
    ]
    return render_template("index.html", title="Home", posts=posts)


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
    if current_user.is_authenticated:  # type: ignore
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:  # type: ignore
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)  # type: ignore
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/user/list", methods=["GET"])
@login_required
def view_users() -> str:
    form = UserForm()
    users = User.query.order_by(User.date_added)
    return render_template("view_users.html", form=form, users=users)
