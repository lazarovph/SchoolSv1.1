from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    username = StringField('Потребителско име', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Имейл', validators=[DataRequired(), Email()])
    phone = StringField('Телефонен номер', validators=[DataRequired(), Length(min=10, max=15)])
    role = RadioField('Роля', choices=[('student', 'Ученика'), ('teacher', 'Учителя')], default='student')
    password = PasswordField('Парола', validators=[DataRequired(), Length(min=6, max=20)])
    submit = SubmitField('Регистрация')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
