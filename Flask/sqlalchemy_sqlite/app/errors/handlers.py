from typing import Literal

from app import app, db
from flask import render_template


@app.errorhandler(404)
def not_found_error(error) -> tuple[str, Literal[404]]:
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def internal_error(error) -> tuple[str, Literal[500]]:
    db.session.rollback()
    return render_template("errors/500.html"), 500
