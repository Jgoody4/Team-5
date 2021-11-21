from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8, message='Password must be at least 8 characters!')
        ]
    )
    confirm = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo(password, message='Passwords must match!')
        ]
    )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ]
    )
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign-in')
