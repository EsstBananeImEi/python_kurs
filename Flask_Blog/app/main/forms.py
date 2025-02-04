from app.auth.forms import EditUserForm
from app.models import User
from flask import request
from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError


class SearchForm(FlaskForm):
    q = StringField(_l("Search"), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if "formdata" not in kwargs:
            kwargs["formdata"] = request.args
        if "meta" not in kwargs:
            kwargs["meta"] = {"csrf": False}
        super(SearchForm, self).__init__(*args, **kwargs)


class EmptyForm(FlaskForm):
    submit = SubmitField(_l("Submit"))


class PostForm(FlaskForm):
    post = TextAreaField(
        _l("Your Message"),
        validators=[DataRequired(), Length(min=1, max=300)],
    )
    submit = SubmitField(_l("Submit"))


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


class MessageForm(FlaskForm):
    message = TextAreaField(
        _l("Message"), validators=[DataRequired(), Length(min=0, max=140)]
    )
    submit = SubmitField(_l("Submit"))
