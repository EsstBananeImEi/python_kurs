from datetime import datetime
from xmlrpc.client import DateTime

from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.urls import url_parse

from app import app, db
from app.forms import (
    AdminForm,
    EditProfileForm,
    EditUserForm,
    EmptyForm,
    LoginForm,
    NameForm,
    RegistrationForm,
)
from app.models import User


@app.errorhandler(404)
def not_found_error(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template("errors/500.html"), 500


@app.before_request
def before_request():
    if current_user.is_authenticated:  # type: ignore
        current_user.last_seen = datetime.now()
        db.session.commit()


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


@app.route("/user/<username>")
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {
            "author": user,
            "body": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "timestamp": datetime.now(),
        },
        {
            "author": user,
            "body": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "timestamp": datetime.now(),
        },
    ]
    form = EmptyForm()
    return render_template("user/user.html", user=user, posts=posts, form=form)


@app.context_processor
def utility_processor():
    def last_seen(date: datetime, format="%d.%m.%Y - %H:%M:%S"):
        if date is None:
            return "User not seen yet"
        last_seen = datetime.strptime(date.strftime(format), format)
        diff = datetime.now() - last_seen

        if diff.total_seconds() <= 30:
            return "Now Online"
        return date.strftime(format)

    def format_date(date: datetime, format="%d.%m.%Y - %H:%M:%S"):
        return datetime.strptime(date.strftime(format), format)

    return dict(last_seen=last_seen, format_date=format_date)


@app.route("/edit_profile/<int:id>", methods=["GET", "POST"])
@login_required
def edit_profile(id):
    form = EditProfileForm(current_user.username)  # type: ignore
    user = User.query.get_or_404(id)
    if not id == current_user.id:  # type: ignore
        return redirect(url_for("user", username=current_user.username))  # type: ignore
    form.about_me.data = user.about_me
    if request.method == "POST":
        user.firstname = request.form["firstname"]
        user.lastname = request.form["lastname"]
        user.username = request.form["username"]
        user.email = request.form["email"]
        user.about_me = request.form["about_me"]
        if len(request.form["password"]) != 0:
            user.password_hash = generate_password_hash(request.form["password"])

        user.last_modify = datetime.now()

        if form.validate_on_submit():
            db.session.commit()
            flash("Deine änderungen wurden gespeichert.")
            user = User.query.get_or_404(id)
            return redirect(url_for("edit_profile", id=user.id))
        return render_template(
            "user/edit_profile.html", title="Edit Profile", form=form, user=user
        )
    return render_template(
        "user/edit_profile.html", title="Edit Profile", form=form, user=user
    )


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
    if id == current_user.id:  # type: ignore
        flash("Den eigenen Nutzer Löschen ist nicht erlaubt!")
        return redirect(url_for("view_users"))  # type: ignore
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


@app.route("/follow/<username>", methods=["POST"])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash("User {} not found.".format(username))
            return redirect(url_for("index"))
        if user == current_user:
            flash("You cannot follow yourself!")
            return redirect(url_for("user", username=username))
        current_user.follow(user)  # type: ignore
        db.session.commit()
        flash("You are following {}!".format(username))
        return redirect(url_for("user", username=username))
    else:
        return redirect(url_for("index"))


@app.route("/unfollow/<username>", methods=["POST"])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash("User {} not found.".format(username))
            return redirect(url_for("index"))
        if user == current_user:
            flash("You cannot unfollow yourself!")
            return redirect(url_for("user", username=username))
        current_user.unfollow(user)  # type: ignore
        db.session.commit()
        flash("You are not following {}.".format(username))
        return redirect(url_for("user", username=username))
    else:
        return redirect(url_for("index"))
