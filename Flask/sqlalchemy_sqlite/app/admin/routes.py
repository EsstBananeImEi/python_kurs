import sqlite3
from datetime import datetime
from typing import Callable

import sqlalchemy
from app import db
from app.admin import admin_blueprint
from app.auth.forms import AdminForm, EditUserForm
from app.main.forms import SearchForm
from app.models import Post, User
from flask import current_app, flash, g, redirect, render_template, request, url_for
from flask_babel import _, get_locale
from flask_login import current_user, login_required
from werkzeug import Response
from werkzeug.security import generate_password_hash


@admin_blueprint.before_request
def before_request():
    if current_user.is_authenticated:  # type: ignore
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
        g.search_form = SearchForm()
    g.locale = str(get_locale())


@admin_blueprint.route("/register/user", methods=["GET", "POST"])
@login_required
def add_user() -> str | Response:
    form = EditUserForm()
    if form.validate_on_submit():
        message = ""
        message_categorie = "info"
        user = User(
            firstname=request.form.get("firstname"),
            lastname=request.form.get("lastname"),
            username=request.form.get("username"),
            email=request.form.get("email"),
            administrator=True if request.form.get("admin") == "y" else False,
        )  # type: ignore
        try:
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            message = _("User was successfully created!")
            message_categorie = "success"

            return redirect(url_for("admin.view_users"))
        except sqlalchemy.exc.IntegrityError:
            message = _("There is already a user with this email!")
            message_categorie = "danger"
            db.session.rollback()
        except Exception:
            message = _("Whoops! There was a prssoblem!")
            message_categorie = "danger"
            db.session.rollback()
        finally:
            flash(message, message_categorie)
    return render_template("admin/add_user.html", title=_("Add New User"), form=form)


@admin_blueprint.route("/user/list", methods=["GET"])
@login_required
def view_users() -> str | Response:
    if not current_user.administrator:  # type: ignore
        return redirect(url_for("main.index"))
    form = AdminForm()
    users = User.query.order_by(User.id)
    return render_template("admin/view_users.html", form=form, users=users)


@admin_blueprint.route("/delete/<int:id>")
@login_required
def delete(id):
    user = User.query.get_or_404(id)
    if current_user.administrator:  # type: ignore
        if id == current_user.id:  # type: ignore
            flash(_("Deleting the own user is not allowed!"), "danger")
            return redirect(url_for("admin.view_users"))  # type: ignore
        try:
            db.session.delete(user)
            db.session.commit()
            flash(_("User was successfully deleted!"), "success")
        except:
            flash(_("Whoops! There was a problem!"), "danger")
        finally:
            return redirect(url_for("admin.view_users"))
    return redirect(url_for("main.index"))


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
                    _("{username} Successfully edited!").format(username=user.username),
                    "success",
                )
                return redirect(url_for("admin.view_users"))

            return render_template(
                "user/edit.html", form=form, user=user, id=id, is_admin=is_admin
            )
        except sqlalchemy.exc.IntegrityError as e:
            flash(str(e), "danger")
            db.session.rollback()
            return redirect(url_for("admin.view_users"))
        except Exception:
            flash(_("Error! A problem has occurred!"), "danger")
            return redirect(url_for("admin.view_users"))

    else:
        return render_template(
            "admin/edit.html", form=form, user=user, id=id, is_admin=is_admin
        )
