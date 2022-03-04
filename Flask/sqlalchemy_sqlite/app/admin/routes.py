from datetime import datetime
from typing import Callable, Literal
from xmlrpc.client import DateTime

from app import db
from app.admin import admin_blueprint
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


@admin_blueprint.route("/register/user", methods=["GET", "POST"])
@login_required
def add_user() -> str | Response:
    form = EditUserForm()
    if form.validate_on_submit():
        user = User(
            firstname=request.form.get("firstname"),
            lastname=request.form.get("lastname"),
            username=request.form.get("username"),
            email=request.form.get("email"),
            administrator=True if request.form.get("admin") == "y" else False,
        )  # type: ignore
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(_("User was successfully created!"))
        return redirect(url_for("view_users"))
    return render_template("admin/add_user.html", title=_("Add New User"), form=form)


@admin_blueprint.route("/user/list", methods=["GET"])
@login_required
def view_users() -> str | Response:
    if not current_user.administrator:  # type: ignore
        return redirect(url_for("main.index"))
    form = AdminForm()
    users = User.query.order_by(User.id)
    return render_template("admin/view_users.html", form=form, users=users)


@admin_blueprint.route("/user/list/<int:id>")
@login_required
def delete(id):
    print(id)
    user = User.query.get_or_404(id)
    if id == current_user.id:  # type: ignore
        flash(_("Deleting the own user is not allowed!"))
        return redirect(url_for("view_users"))  # type: ignore
    form = AdminForm()
    users = None
    try:
        db.session.delete(user)
        db.session.commit()
        flash(_("User was successfully deleted!"))
        users = User.query.order_by(User.id)
    except:
        flash(_("Whoops! There was a problem!"))
    finally:
        return render_template("admin/view_users.html", form=form, users=users)


@admin_blueprint.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
    if not current_user.administrator:  # type: ignore
        return redirect(url_for("main.index"))
    form = EditUserForm()
    user = User.query.get_or_404(id)
    users = User.query.order_by(User.id)
    is_admin = user.administrator == 1
    if request.method == "POST":
        user.username = request.form["username"]
        user.email = request.form["email"]
        if not current_user.id == id:  # type: ignore
            user.administrator = True if request.form.get("admin") == "y" else False
        if len(request.form["password"]) != 0:
            user.password_hash = generate_password_hash(request.form["password"])

        user.last_modify = datetime.now()
        try:
            if form.validate_on_submit():
                db.session.commit()
                flash(
                    _("{username} Successfully edited!").format(username=user.username)
                )
                return redirect(url_for("admin.view_users"))

            return render_template(
                "user/edit.html", form=form, user=user, id=id, is_admin=is_admin
            )
        except Exception as e:
            print(e)
            flash(_("Error! A problem has occurred!"))
            return redirect(url_for("main.index"))
    else:
        return render_template(
            "admin/edit.html", form=form, user=user, id=id, is_admin=is_admin
        )
