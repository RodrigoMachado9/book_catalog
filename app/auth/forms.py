# app/auth/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from app.auth.models import User


def email_exists(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email Already Exists')


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(3, 15, message='between 3 to 15 characters')])
    email = StringField('Email', validators=[DataRequired(), Email(), email_exists])
    # email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(5), EqualTo('confirm', message='password must match')])
    confirm = PasswordField('Confirm', validators=[DataRequired()])
    submit = SubmitField('Register')
