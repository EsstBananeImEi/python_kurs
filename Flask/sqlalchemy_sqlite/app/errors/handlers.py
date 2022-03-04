from typing import Literal
from flask import current_app
from app import db
from flask import render_template


@current_app.errorhandler(404)
def not_found_error(error) -> tuple[str, Literal[404]]:
    return render_template("errors/404.html"), 404


@current_app.errorhandler(500)
def internal_error(error) -> tuple[str, Literal[500]]:
    db.session.rollback()
    return render_template("errors/500.html"), 500
