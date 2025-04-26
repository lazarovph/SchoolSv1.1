from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class CourseForm(FlaskForm):
    name = StringField('Course Name', validators=[DataRequired()])
    description = TextAreaField('Course Description')
    level_id = SelectField('Level', coerce=int)
    submit = SubmitField('Submit')

class LevelForm(FlaskForm):
    name = StringField('Level Name', validators=[DataRequired()])
    description = TextAreaField('Level Description')
    submit = SubmitField('Submit')
