from datetime import datetime
from xmlrpc.client import DateTime

from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.urls import url_parse

from app import app, db
from app.forms import AdminForm, EditUserForm, LoginForm, NameForm, RegistrationForm
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
    return render_template("restricted_pages/index.html", title="Home", posts=posts)


@app.route("/user/name/<name>")
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
    return render_template("user/login.html", title="Sign In", form=form)


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
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, username=form.username.data, email=form.email.data)  # type: ignore
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Gratulation, Sie sind jetzt ein Registrierter Nutzer!")
        return redirect(url_for("login"))
    return render_template("user/register.html", title="Register", form=form)


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
        flash("Nutzer wurde hinzugefügt!")
        return redirect(url_for("view_users"))
    return render_template(
        "restricted_pages/add_user.html", title="Add New User", form=form
    )


@app.route("/user/list", methods=["GET"])
@login_required
def view_users() -> str:
    form = AdminForm()
    users = User.query.order_by(User.id)
    return render_template("restricted_pages/view_users.html", form=form, users=users)


@app.route("/user/list/<int:id>")
@login_required
def delete(id):
    print(id)
    user = User.query.get_or_404(id)
    form = AdminForm()
    users = None
    try:
        db.session.delete(user)
        db.session.commit()
        flash("Nutzer wurde erfolgreich gelöscht!")
        users = User.query.order_by(User.id)
    except:
        flash("Whoops! Es gab ein Problem!")
    finally:
        return render_template(
            "restricted_pages/view_users.html", form=form, users=users
        )


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
                flash(f"Nutzer: {user.username} Erfolgreich bearbeitet!")
                users = User.query.order_by(User.id)
                return render_template(
                    "restricted_pages/view_users.html", form=form, users=users
                )
            return render_template(
                "user/edit.html", form=form, user=user, id=id, is_admin=is_admin
            )
        except:
            flash("Error! Ein Problem ist aufgetreten!")
            return render_template(
                "restricted_pages/view_users.html", form=form, users=users
            )
    else:
        return render_template(
            "user/edit.html", form=form, user=user, id=id, is_admin=is_admin
        )
