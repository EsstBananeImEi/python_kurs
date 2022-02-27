from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    Optional,
    Regexp,
    ValidationError,
)

from app.models import User


class NameForm(FlaskForm):
    name: StringField = StringField("Wie ist dein name", validators=[DataRequired()])
    submit: SubmitField = SubmitField("Submit")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class UserForm(FlaskForm):
    username: StringField = StringField("Username", validators=[DataRequired()])
    firstname: StringField = StringField("Vorname", validators=[DataRequired()])
    lastname: StringField = StringField("Nachname", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    admin = BooleanField("Administrator", validators=[])
    submit: SubmitField = SubmitField("Submit")


class EditUserForm(FlaskForm):
    firstname: StringField = StringField("Vorname", validators=[DataRequired()])
    lastname: StringField = StringField("Nachname", validators=[DataRequired()])
    username: StringField = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Passwort",
        validators=[
            Optional(),
            Length(min=8, message="Password be at least 8 characters"),
            Regexp("^(?=.*[a-z])", message="Passwort muss Kleinbuchstaben enthalten"),
            Regexp("^(?=.*[A-Z])", message="Passwort muss Großbuchstaben enthalten"),
            Regexp("^(?=.*\\d)", message="Passwort muss Zahlen enthalten"),
            Regexp("(?=.*[@$!%*#?&])", message="Passwort muss Zeichen enthalten"),
        ],
    )
    password2 = PasswordField(
        "Passwort wiederholen", validators=[Optional(), EqualTo("password")]
    )
    admin = BooleanField("Administrator", validators=[])
    submit: SubmitField = SubmitField("Submit")


class RegistrationForm(FlaskForm):
    firstname: StringField = StringField(
        "Vorname",
        validators=[
            DataRequired(),
        ],
    )
    lastname: StringField = StringField("Nachname", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Passwort",
        validators=[
            DataRequired(),
            Length(min=8, message="Password be at least 8 characters"),
            Regexp("^(?=.*[a-z])", message="Passwort muss Kleinbuchstaben enthalten"),
            Regexp("^(?=.*[A-Z])", message="Passwort muss Großbuchstaben enthalten"),
            Regexp("^(?=.*\\d)", message="Passwort muss Zahlen enthalten"),
            Regexp("(?=.*[@$!%*#?&])", message="Passwort muss Zeichen enthalten"),
        ],
    )
    password2 = PasswordField(
        "Repeat Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Please use a different username.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Please use a different email address.")
