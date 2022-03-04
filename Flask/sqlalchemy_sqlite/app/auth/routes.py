from datetime import datetime
from typing import Callable, Literal
from xmlrpc.client import DateTime

from app import db
from app.auth import auth_blueprint
from app.auth.email import send_password_reset_email
from app.auth.forms import (
    AdminForm,
    EditUserForm,
    LoginForm,
    NameForm,
    RegistrationForm,
    ResetPasswordForm,
    ResetPasswordRequestForm,
)
from app.models import Post, User
from flask import flash, g, redirect, render_template, request, url_for
from flask_babel import _, get_locale
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug import Response
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.urls import url_parse


@auth_blueprint.route("/reset_password_request", methods=["GET", "POST"])
def reset_password_request() -> str | Response:
    if current_user.is_authenticated:  # type: ignore
        return redirect(url_for("main.index"))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash(_("Check your email for the instructions to reset your password"))
        return redirect(url_for("auth.login"))
    return render_template(
        "auth/reset_password_request.html", title="Reset Password", form=form
    )


@auth_blueprint.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token) -> str | Response:
    if current_user.is_authenticated:  # type: ignore
        return redirect(url_for("main.index"))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for("main.index"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash(_("Your password has been reset."))
        return redirect(url_for("auth.login"))
    return render_template("auth/reset_password.html", form=form)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login() -> str | Response:
    if current_user.is_authenticated:  # type: ignore
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(_("Invalid username or password"))
            return redirect(url_for("auth.login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("main.index")
        return redirect(next_page)
    return render_template("auth/login.html", title="Sign In", form=form)


@auth_blueprint.route("/logout")
def logout() -> Response:
    logout_user()
    return redirect(url_for("main.index"))


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register() -> str | Response:
    if current_user.is_authenticated:  # type: ignore
        return redirect(url_for("main.index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, username=form.username.data, email=form.email.data)  # type: ignore
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(_("Congratulations, you are now a registered user!"))
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", title="Register", form=form)
