from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    due_date = DateField('Due Date')
    submit = SubmitField('Submit')

