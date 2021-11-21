from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TimeInserted(FlaskForm):
	inserted_time = StringField('Time', validators=[DataRequired()])
	submit = SubmitField('Submit')
