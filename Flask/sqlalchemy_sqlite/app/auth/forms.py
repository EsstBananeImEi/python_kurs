from flask_babel import lazy_gettext as _l
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
    submit = SubmitField(_l("Submit"))


class PostForm(FlaskForm):
    post = TextAreaField(
        _l("Your Message"),
        validators=[DataRequired(), Length(min=1, max=140)],
    )
    submit = SubmitField(_l("Submit"))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l("Email"), validators=[DataRequired(), Email()])
    submit = SubmitField(_l("Request Password Reset"))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(
        _l("Password"),
        validators=[
            DataRequired(),
            Length(min=8, message=_l("Password be at least 8 characters")),
            Regexp(
                "^(?=.*[a-z])",
                message=_l("Password must contain lowercase letters"),
            ),
            Regexp(
                "^(?=.*[A-Z])",
                message=_l("Password must contain capital letters"),
            ),
            Regexp("^(?=.*\\d)", message=_l("Password must contain numbers")),
            Regexp(
                "(?=.*[@$!%*#?&])",
                message=_l("Password must contain characters"),
            ),
        ],
    )
    password2 = PasswordField(
        _l("Repeat Password"),
        validators=[DataRequired(), EqualTo("password")],
    )
    submit = SubmitField(_l("Request Password Reset"))


class NameForm(FlaskForm):
    name: StringField = StringField(
        _l("What is your name"), validators=[DataRequired()]
    )
    submit: SubmitField = SubmitField(_l("Submit"))


class LoginForm(FlaskForm):
    username = StringField(_l("Username"), validators=[DataRequired()])
    password = PasswordField(_l("Password"), validators=[DataRequired()])
    remember_me = BooleanField(_l("Remember Me"))
    submit = SubmitField(_l("Sign In"))


class BasicForm(FlaskForm):
    username: StringField = StringField(_l("Username"), validators=[DataRequired()])
    firstname: StringField = StringField(_l("Firstname"), validators=[DataRequired()])
    lastname: StringField = StringField(_l("Lastname"), validators=[DataRequired()])
    email = StringField(_l("Email"), validators=[DataRequired(), Email()])
    submit: SubmitField = SubmitField(_l("Submit"))


class AdminForm(BasicForm):
    admin = BooleanField(_l("Administrator"), validators=[])


class RegistrationForm(BasicForm):
    password = PasswordField(
        _l("Password"),
        validators=[
            DataRequired(),
            Length(min=8, message=_l("Password be at least 8 characters")),
            Regexp(
                "^(?=.*[a-z])",
                message=_l("Password must contain lowercase letters"),
            ),
            Regexp(
                "^(?=.*[A-Z])",
                message=_l("Password must contain capital letters"),
            ),
            Regexp("^(?=.*\\d)", message=_l("Password must contain numbers")),
            Regexp(
                "(?=.*[@$!%*#?&])",
                message=_l("Password must contain characters"),
            ),
        ],
    )
    password2 = PasswordField(
        _l("Repeat Password"),
        validators=[DataRequired(), EqualTo("password")],
    )

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_l("Please use a different username."))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_l("Please use a different email address."))


class EditUserForm(AdminForm):
    password = PasswordField(
        _l("Password"),
        validators=[
            Optional(),
            Length(min=8, message=_l("Password be at least 8 characters")),
            Regexp(
                "^(?=.*[a-z])",
                message=_l("Password must contain lowercase letters"),
            ),
            Regexp(
                "^(?=.*[A-Z])",
                message=_l("Password must contain capital letters"),
            ),
            Regexp("^(?=.*\\d)", message=_l("Password must contain numbers")),
            Regexp(
                "(?=.*[@$!%*#?&])",
                message=_l("Password must contain characters"),
            ),
        ],
    )
    password2 = PasswordField(
        _l("Repeat Password"), validators=[Optional(), EqualTo("password")]
    )


class EditProfileForm(EditUserForm):
    about_me = TextAreaField(_l("About me"), validators=[Length(min=0, max=140)])

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_l("Please use a different username."))
