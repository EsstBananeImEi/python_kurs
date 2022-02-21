import sqlite3

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort


def get_db_connection() -> sqlite3.Connection:
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    return connection


app = Flask(__name__)
app.config["SECRET_KEY"] = "your secret key"


@app.route("/")
def index():
    connection = get_db_connection()
    posts = connection.execute("SELECT * FROM posts").fetchall()
    connection.close
    return render_template("index.html", posts=posts)


def get_post(post_id: int):
    conn = get_db_connection()
    post = conn.execute(f"SELECT * FROM posts WHERE id = {post_id}").fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route("/<int:post_id>", methods=["PUT"])
def set_view_state(post_id: int):
    conn = get_db_connection()
    post = conn.execute(f"UPDATE posts SET viewed=1 WHERE id={post_id}").fetchone()
    conn.commit()


@app.route("/<int:post_id>")
def post(post_id: int):
    post = get_post(post_id)
    if post is not None:
        set_view_state(post)
    return render_template("post.html", post=post)


@app.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title:
            flash("Title is required!")
        else:
            conn = get_db_connection()
            conn.execute(
                f"INSERT INTO posts (title, content) VALUES ('{title}', '{content}')"
            )
            conn.commit()
            conn.close()
            return redirect(url_for("index"))
    return render_template("create.html")


@app.route("/<int:id>/edit", methods=("GET", "POST"))
def edit(id: int):
    post = get_post(id)

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title:
            flash("Title is required!")
        else:
            conn = get_db_connection()
            conn.execute(
                "UPDATE posts SET title = ?, content = ?" " WHERE id = ?",
                (title, content, id),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("index"))

    return render_template("edit.html", post=post)


# ....


@app.route("/<int:id>/delete", methods=("POST",))
def delete(id: int):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute(f"DELETE FROM posts WHERE id = {id}")
    conn.commit()
    conn.close()
    flash(f'"{post["title"]}" was successfully deleted!')
    return redirect(url_for("index"))
