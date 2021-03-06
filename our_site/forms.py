from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired, EqualTo, InputRequired

class DateForm(FlaskForm):
    # A textbox to input a date and time for study blocks.
    name = StringField(
        'Event Name'
    )
    start_date = DateTimeLocalField(
        'Start Date/Time',
        format='%Y-%m-%dT%H:%M'
    )
    end_date = DateTimeLocalField(
        'End Date/Time',
        format='%Y-%m-%dT%H:%M'
    )
    submit = SubmitField('Submit')

class MailingForm(FlaskForm):
    file = FileField(
        'File Upload',
        validators=[
            FileRequired(),
            FileAllowed(['md', 'pdf'], '.md and .pdf files only!')
        ]
    )
    submit = SubmitField('Upload and Email')

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

class Markdown(FlaskForm):
    title = StringField('Title: ', validators= [DataRequired()])
    markdown = StringField('Markdown:', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
    # Textboxes used to enter a username and password to save for registration
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
    # Textboxes used to login a user, checking their credentials to see if they
    # exist in the database already, and determines whether or not to remember
    # username and password
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
