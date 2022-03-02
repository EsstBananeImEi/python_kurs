from datetime import datetime
from typing import Callable
from xmlrpc.client import DateTime

from app import app, db
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
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.urls import url_parse


@app.errorhandler(404)
def not_found_error(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template("errors/500.html"), 500


@app.route("/reset_password_request", methods=["GET", "POST"])
def reset_password_request():
    if current_user.is_authenticated:  # type: ignore
        return redirect(url_for("main.index"))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash(_("Check your email for the instructions to reset your password"))
        return redirect(url_for("login"))
    return render_template(
        "auth/reset_password_request.html", title="Reset Password", form=form
    )


@app.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
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
        return redirect(url_for("login"))
    return render_template("auth/reset_password.html", form=form)


@app.context_processor
def utility_processor() -> dict[str, Callable]:
    """
    Utility Processor ermöglicht die benutzung von eigenen Funktionen im HTML
    usage:
        @app.context_processor
        def utility_processor() -> dict[str, Callable]:
            def myFunction(arg):
                ...
                return
            return dict(myFunction=myFunction)

    return: dict[str, Callable]
    """
    return dict()


@app.route("/name", methods=["GET", "POST"])
def name_form() -> str:
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash(_("Form Successfully Sent"))

    return render_template("name.html", name=name, form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:  # type: ignore
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(_("Invalid username or password"))
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("main.index")
        return redirect(next_page)
    return render_template("auth/login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:  # type: ignore
        return redirect(url_for("main.index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, username=form.username.data, email=form.email.data)  # type: ignore
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(_("Congratulations, you are now a registered user!"))
        return redirect(url_for("login"))
    return render_template("auth/register.html", title="Register", form=form)


@app.route("/register/user", methods=["GET", "POST"])
@login_required
def add_user():
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


@app.route("/user/list", methods=["GET"])
@login_required
def view_users() -> str:
    form = AdminForm()
    users = User.query.order_by(User.id)
    return render_template("admin/view_users.html", form=form, users=users)


@app.route("/user/list/<int:id>")
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


@app.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
    form = EditUserForm()
    user = User.query.get_or_404(id)
    users = User.query.order_by(User.id)
    is_admin = user.administrator == 1
    if request.method == "POST":
        user.username = request.form["username"]
        user.email = request.form["email"]
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
                users = User.query.order_by(User.id)
                return render_template("admin/view_users.html", form=form, users=users)
            return render_template(
                "user/edit.html", form=form, user=user, id=id, is_admin=is_admin
            )
        except:
            flash(_("Error! A problem has occurred!"))
            return render_template("admin/view_users.html", form=form, users=users)
    else:
        return render_template(
            "user/edit.html", form=form, user=user, id=id, is_admin=is_admin
        )
