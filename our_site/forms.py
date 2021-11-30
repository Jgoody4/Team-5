from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, InputRequired

class TimeInserted(FlaskForm):
	# A textbox to insert time and a submit button, both used for the timer.
	inserted_time = StringField('Time', validators=[DataRequired()])
	submit = SubmitField('Submit')

class Shuffling(FlaskForm):
	# A shuffle button used to shuffle the order of the flashcards.
	shuffler = SubmitField('Shuffle')

class FlashCards(FlaskForm):
	# Textboxes for the term and description of a flashcard, and a submit button.
	# These are used to create flashcards.
	card_term = StringField('Term', validators=[DataRequired()])
	card_def = StringField('Definition', validators=[DataRequired()])
	submit = SubmitField('Submit')

class Reminder(FlaskForm):
    # Textboxes used to enter reminder task and reminder time
    reminder_task = StringField ('Reminder Task: ', validators= [DataRequired()])
    reminder_time = StringField('Time (00:00)', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Match(FlaskForm):
    # Textbox used to enter the answer/definition to a term when matching terms to 
    # definitions
    answer = StringField('Answer', validators= [DataRequired()])
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
