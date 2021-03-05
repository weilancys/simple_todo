from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


def new_todo_not_blank(form, field):
    if field.data.strip() == "":
        raise ValidationError("new todo item is blank.")


class SignUpForm(FlaskForm):
    email = EmailField("email", validators=[DataRequired(), Email()])
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    confirm_password = PasswordField("confirm password", validators=[DataRequired(), EqualTo("password", "passwords don't match.")])


class LoginForm(FlaskForm):
    email = EmailField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])


class NewTodoForm(FlaskForm):
    new_todo = StringField("new-todo", validators=[DataRequired(), new_todo_not_blank])


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('old password', validators=[DataRequired()])
    new_password = PasswordField('new password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(), EqualTo('new_password', 'passwords do not match')])


class TodoListForm(FlaskForm):
    pass
