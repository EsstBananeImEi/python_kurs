from datetime import datetime
from typing import Callable
from xmlrpc.client import DateTime

from flask import flash, redirect, render_template, request, url_for
from flask_babel import _
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.urls import url_parse

from app import app, db
from app.email import send_password_reset_email
from app.forms import (
    AdminForm,
    EditProfileForm,
    EditUserForm,
    EmptyForm,
    LoginForm,
    NameForm,
    PostForm,
    RegistrationForm,
    ResetPasswordForm,
    ResetPasswordRequestForm,
)
from app.models import Post, User


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
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route("/reset_password_request", methods=["GET", "POST"])
def reset_password_request():
    if current_user.is_authenticated:  # type: ignore
        return redirect(url_for("index"))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash(_("Check your email for the instructions to reset your password"))
        return redirect(url_for("login"))
    return render_template(
        "user/reset_password_request.html", title="Reset Password", form=form
    )


@app.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:  # type: ignore
        return redirect(url_for("index"))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for("index"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash(_("Your password has been reset."))
        return redirect(url_for("login"))
    return render_template("user/reset_password.html", form=form)


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash(_("Your post is now live!"))
        return redirect(url_for("index"))
    page = request.args.get("page", 1, type=int)
    posts = current_user.followed_posts().paginate(page, app.config["POSTS_PER_PAGE"], False)  # type: ignore
    next_url = url_for("index", page=posts.next_num) if posts.has_next else None
    prev_url = url_for("index", page=posts.prev_num) if posts.has_prev else None
    return render_template(
        "restricted_pages/index.html",
        title="Home",
        form=form,
        posts=posts.items,
        next_url=next_url,
        prev_url=prev_url,
    )


@app.route("/explore")
@login_required
def explore():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, app.config["POSTS_PER_PAGE"], False
    )
    next_url = url_for("explore", page=posts.next_num) if posts.has_next else None
    prev_url = url_for("explore", page=posts.prev_num) if posts.has_prev else None
    return render_template(
        "restricted_pages/index.html",
        title=_("Explore"),
        posts=posts.items,
        next_url=next_url,
        prev_url=prev_url,
    )


@app.route("/user/<username>")
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get("page", 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, app.config["POSTS_PER_PAGE"], False
    )
    next_url = (
        url_for("user", username=user.username, page=posts.next_num)
        if posts.has_next
        else None
    )
    prev_url = (
        url_for("user", username=user.username, page=posts.prev_num)
        if posts.has_prev
        else None
    )
    form = EmptyForm()
    return render_template(
        "user/user.html",
        user=user,
        posts=posts.items,
        next_url=next_url,
        prev_url=prev_url,
        form=form,
    )


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
            flash(_("Your changes have been saved."))
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
        flash(_("Form Successfully Sent"))

    return render_template("name.html", name=name, form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:  # type: ignore
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(_("Invalid username or password"))
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
        flash(_("Congratulations, you are now a registered user!"))
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
        flash(_("User was successfully created!"))
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
                flash(_(f"{user.username} Successfully edited!"))
                users = User.query.order_by(User.id)
                return render_template(
                    "restricted_pages/view_users.html", form=form, users=users
                )
            return render_template(
                "user/edit.html", form=form, user=user, id=id, is_admin=is_admin
            )
        except:
            flash(_("Error! A problem has occurred!"))
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
            flash(_(f"User {username} not found."))
            return redirect(url_for("index"))
        if user == current_user:
            flash(_("You cannot follow yourself!"))
            return redirect(url_for("user", username=username))
        current_user.follow(user)  # type: ignore
        db.session.commit()
        flash(_(f"You are following {username}!"))
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
            flash(_(f"User {username} not found."))
            return redirect(url_for("index"))
        if user == current_user:
            flash(_("You cannot unfollow yourself!"))
            return redirect(url_for("user", username=username))
        current_user.unfollow(user)  # type: ignore
        db.session.commit()
        flash(_(f"You are not following {username}."))
        return redirect(url_for("user", username=username))
    else:
        return redirect(url_for("index"))
