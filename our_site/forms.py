from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, InputRequired

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
            InputRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            InputRequired()
        ]
    )
    confirm = PasswordField(
        'Confirm Password',
        validators=[
            InputRequired(),
            EqualTo('password', message='Passwords must match!')
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
