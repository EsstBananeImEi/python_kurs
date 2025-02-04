from threading import Thread

from app import mail
from flask import current_app, render_template
from flask_babel import _
from flask_mail import Message


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(
        _("[Flask Blog] Reset Your Password"),
        sender=current_app.config["SENDER_EMAIL"],
        recipients=[user.email],
        text_body=render_template("email/reset_password.txt", user=user, token=token),
        html_body=render_template("email/reset_password.html", user=user, token=token),
    )


def send_user_deleted_email(user):
    token = user.get_reset_password_token()
    send_email(
        _("[Flask Blog] Account was Deleted"),
        sender=current_app.config["SENDER_EMAIL"],
        recipients=[user.email],
        text_body=render_template("email/deleted_user.txt", user=user, token=token),
        html_body=render_template("email/deleted_user.html", user=user, token=token),
    )


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(
        target=send_async_email, args=(current_app._get_current_object(), msg)  # type: ignore
    ).start()
