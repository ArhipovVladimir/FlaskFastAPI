from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class ProcessForm(FlaskForm):
    name = StringField('Содержание процесса', validators=[DataRequired()])



# class ReestrProcss(FlaskForm):
#     username = StringField('Userame', validators=[DataRequired()])
#     name = StringField('Name', validators=[DataRequired()])
#     surname = StringField('Surname', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
