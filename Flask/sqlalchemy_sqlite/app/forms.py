from flask_babel import lazy_gettext
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
    submit = SubmitField(lazy_gettext("Submit"))


class PostForm(FlaskForm):
    post = TextAreaField(
        lazy_gettext("Your Message"),
        validators=[DataRequired(), Length(min=1, max=140)],
    )
    submit = SubmitField(lazy_gettext("Submit"))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(lazy_gettext("Email"), validators=[DataRequired(), Email()])
    submit = SubmitField(lazy_gettext("Request Password Reset"))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(
        lazy_gettext("Password"),
        validators=[
            DataRequired(),
            Length(min=8, message=lazy_gettext("Password be at least 8 characters")),
            Regexp(
                "^(?=.*[a-z])",
                message=lazy_gettext("Password must contain lowercase letters"),
            ),
            Regexp(
                "^(?=.*[A-Z])",
                message=lazy_gettext("Password must contain capital letters"),
            ),
            Regexp("^(?=.*\\d)", message=lazy_gettext("Password must contain numbers")),
            Regexp(
                "(?=.*[@$!%*#?&])",
                message=lazy_gettext("Password must contain characters"),
            ),
        ],
    )
    password2 = PasswordField(
        lazy_gettext("Repeat Password"),
        validators=[DataRequired(), EqualTo("password")],
    )
    submit = SubmitField(lazy_gettext("Request Password Reset"))


class NameForm(FlaskForm):
    name: StringField = StringField(
        lazy_gettext("What is your name"), validators=[DataRequired()]
    )
    submit: SubmitField = SubmitField(lazy_gettext("Submit"))


class LoginForm(FlaskForm):
    username = StringField(lazy_gettext("Username"), validators=[DataRequired()])
    password = PasswordField(lazy_gettext("Password"), validators=[DataRequired()])
    remember_me = BooleanField(lazy_gettext("Remember Me"))
    submit = SubmitField(lazy_gettext("Sign In"))


class BasicForm(FlaskForm):
    username: StringField = StringField(
        lazy_gettext("Username"), validators=[DataRequired()]
    )
    firstname: StringField = StringField(
        lazy_gettext("Firstname"), validators=[DataRequired()]
    )
    lastname: StringField = StringField(
        lazy_gettext("Lastname"), validators=[DataRequired()]
    )
    email = StringField(lazy_gettext("Email"), validators=[DataRequired(), Email()])
    submit: SubmitField = SubmitField(lazy_gettext("Submit"))


class AdminForm(BasicForm):
    admin = BooleanField(lazy_gettext("Administrator"), validators=[])


class RegistrationForm(BasicForm):
    password = PasswordField(
        lazy_gettext("Password"),
        validators=[
            DataRequired(),
            Length(min=8, message=lazy_gettext("Password be at least 8 characters")),
            Regexp(
                "^(?=.*[a-z])",
                message=lazy_gettext("Password must contain lowercase letters"),
            ),
            Regexp(
                "^(?=.*[A-Z])",
                message=lazy_gettext("Password must contain capital letters"),
            ),
            Regexp("^(?=.*\\d)", message=lazy_gettext("Password must contain numbers")),
            Regexp(
                "(?=.*[@$!%*#?&])",
                message=lazy_gettext("Password must contain characters"),
            ),
        ],
    )
    password2 = PasswordField(
        lazy_gettext("Repeat Password"),
        validators=[DataRequired(), EqualTo("password")],
    )

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(lazy_gettext("Please use a different username."))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(lazy_gettext("Please use a different email address."))


class EditUserForm(AdminForm):
    password = PasswordField(
        "Passwort",
        validators=[
            Optional(),
            Length(min=8, message=lazy_gettext("Password be at least 8 characters")),
            Regexp(
                "^(?=.*[a-z])",
                message=lazy_gettext("Password must contain lowercase letters"),
            ),
            Regexp(
                "^(?=.*[A-Z])",
                message=lazy_gettext("Password must contain capital letters"),
            ),
            Regexp("^(?=.*\\d)", message=lazy_gettext("Password must contain numbers")),
            Regexp(
                "(?=.*[@$!%*#?&])",
                message=lazy_gettext("Password must contain characters"),
            ),
        ],
    )
    password2 = PasswordField(
        lazy_gettext("Repeat Password"), validators=[Optional(), EqualTo("password")]
    )


class EditProfileForm(EditUserForm):
    about_me = TextAreaField(
        lazy_gettext("About me"), validators=[Length(min=0, max=140)]
    )

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(lazy_gettext("Please use a different username."))
