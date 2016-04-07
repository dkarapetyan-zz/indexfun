from flask_wtf import Form
import wtforms
from wtforms import StringField, \
    PasswordField, BooleanField
from wtforms.validators import DataRequired
from wtforms.validators import Length, Email



class SignupForm(Form):
    email = StringField('Email address',
                        validators=[
                            DataRequired(
                                'Please provide a valid email address'),
                            Length(min=6, message=u'Email address too short'),
                            Email(
                                message=u'That\'s not a valid email address.')])
    password = PasswordField('Pick a secure password',
                             validators=[
                                 DataRequired(),
                                 Length(min=6,
                                        message='Please give a longer '
                                                'password')])
    username = StringField('Choose your username',
                           validators=[DataRequired()])
    agree = BooleanField('I agree to all the Terms of Services',
                         validators=[
                             DataRequired(
                                 u'You must accept our Terms of Service')])
    submit = wtforms.SubmitField("Submit")
