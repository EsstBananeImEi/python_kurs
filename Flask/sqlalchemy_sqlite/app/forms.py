from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
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


class EmptyForm(FlaskForm):
    submit = SubmitField("Submit")


class NameForm(FlaskForm):
    name: StringField = StringField("Wie ist dein name", validators=[DataRequired()])
    submit: SubmitField = SubmitField("Submit")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class BasicForm(FlaskForm):
    username: StringField = StringField("Username", validators=[DataRequired()])
    firstname: StringField = StringField("Vorname", validators=[DataRequired()])
    lastname: StringField = StringField("Nachname", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit: SubmitField = SubmitField("Submit")


class AdminForm(BasicForm):
    admin = BooleanField("Administrator", validators=[])


class RegistrationForm(BasicForm):
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

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Please use a different username.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Please use a different email address.")


class EditUserForm(AdminForm):
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


class EditProfileForm(EditUserForm):
    about_me = TextAreaField("About me", validators=[Length(min=0, max=140)])

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError("Please use a different username.")
