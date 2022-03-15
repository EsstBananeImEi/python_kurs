from datetime import datetime
from typing import Callable

from app import db
from app.main import main_blueprint
from app.main.forms import EditProfileForm, EmptyForm, PostForm, SearchForm
from app.models import Post, User
from flask import current_app, flash, g, redirect, render_template, request, url_for
from flask_babel import _, get_locale
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash


@main_blueprint.context_processor
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


@main_blueprint.before_request
def before_request():
    if current_user.is_authenticated:  # type: ignore
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
        g.search_form = SearchForm()
    g.locale = str(get_locale())


@main_blueprint.route("/search")
@login_required
def search():
    if not g.search_form.validate():
        return redirect(url_for("main.explore"))
    page = request.args.get("page", 1, type=int)
    posts, total = Post.search(
        g.search_form.q.data, page, current_app.config["POSTS_PER_PAGE"]
    )
    next_url = (
        url_for("main.search", search_field=g.search_form.q.data, page=page + 1)
        if total > page * current_app.config["POSTS_PER_PAGE"]
        else None
    )
    prev_url = (
        url_for("main.search", q=g.search_form.q.data, page=page - 1)
        if page > 1
        else None
    )
    return render_template(
        "search.html",
        title=_("Search"),
        total=total,
        posts=posts,
        next_url=next_url,
        prev_url=prev_url,
    )


@main_blueprint.route("/", methods=["GET", "POST"])
@main_blueprint.route("/index", methods=["GET", "POST"])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)  # type:ignore
        db.session.add(post)
        db.session.commit()
        flash(_("Your post is now live!"))
        return redirect(url_for("main.index"))
    page = request.args.get("page", 1, type=int)
    posts = current_user.followed_posts().paginate(page, current_app.config["POSTS_PER_PAGE"], False)  # type: ignore
    next_url = url_for("main.index", page=posts.next_num) if posts.has_next else None
    prev_url = url_for("main.index", page=posts.prev_num) if posts.has_prev else None
    return render_template(
        "index.html",
        title="Home",
        form=form,
        posts=posts.items,
        next_url=next_url,
        prev_url=prev_url,
    )


@main_blueprint.route("/explore")
@login_required
def explore():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config["POSTS_PER_PAGE"], False
    )
    next_url = url_for("main.explore", page=posts.next_num) if posts.has_next else None
    prev_url = url_for("main.explore", page=posts.prev_num) if posts.has_prev else None
    return render_template(
        "index.html",
        title=_("Explore"),
        posts=posts.items,
        next_url=next_url,
        prev_url=prev_url,
    )


@main_blueprint.route("/user/<username>")
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get("page", 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config["POSTS_PER_PAGE"], False
    )
    next_url = (
        url_for("main.user", username=user.username, page=posts.next_num)
        if posts.has_next
        else None
    )
    prev_url = (
        url_for("main.user", username=user.username, page=posts.prev_num)
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


@main_blueprint.route("/edit_profile/<int:id>", methods=["GET", "POST"])
@login_required
def edit_profile(id):
    form = EditProfileForm(current_user.username)  # type: ignore
    user = User.query.get_or_404(id)
    if not id == current_user.id:  # type: ignore
        return redirect(url_for("main.user", username=current_user.username))  # type: ignore
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
            return redirect(url_for("main.edit_profile", id=user.id))
        return render_template(
            "user/edit_profile.html", title="Edit Profile", form=form, user=user
        )
    return render_template(
        "user/edit_profile.html", title="Edit Profile", form=form, user=user
    )


@main_blueprint.route("/follow/<username>", methods=["POST"])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash(_("User {username} not found.").format(username=username))
            return redirect(url_for("main.index"))
        if user == current_user:
            flash(_("You cannot follow yourself!"))
            return redirect(url_for("main.user", username=username))
        current_user.follow(user)  # type: ignore
        db.session.commit()
        flash(_("You are following {username}!").format(username=username))
        return redirect(url_for("main.user", username=username))
    else:
        return redirect(url_for("main.index"))


@main_blueprint.route("/unfollow/<username>", methods=["POST"])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash(_("User {username} not found.").format(username=username))
            return redirect(url_for("main.index"))
        if user == current_user:
            flash(_("You cannot unfollow yourself!"))
            return redirect(url_for("main.user", username=username))
        current_user.unfollow(user)  # type: ignore
        db.session.commit()
        flash(_("You are not following {username}.").format(username=username))
        return redirect(url_for("main.user", username=username))
    else:
        return redirect(url_for("main.index"))
