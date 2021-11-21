from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class TimeInserted(FlaskForm):
	inserted_time = StringField('Time', validators=[DataRequired()])
	submit = SubmitField('Submit')

class Shuffling(FlaskForm):
	shuffler = SubmitField('Shuffle')

class FlashCards(FlaskForm):
	card_term = StringField('Term', validators=[DataRequired()])
	card_def = StringField('Definition', validators=[DataRequired()])
	submit = SubmitField('Submit')

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
