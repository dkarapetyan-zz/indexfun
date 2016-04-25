from flask_wtf import Form
from wtforms import FloatField, BooleanField, SubmitField, StringField

from wtforms.validators import number_range, DataRequired, Length, Regexp

__author__ = 'davidkarapetyan'


class Invest(Form):
    money = FloatField('Amount (in $)', validators=[number_range(min=0)])
    submit = SubmitField('Submit')


class Liquid(Form):
    is_liquid = BooleanField("Make me liquid.")
    submit = SubmitField('Submit')


class AutoInvest(Form):
    is_liquid = BooleanField("Make me AutoInvest.")
    submit = SubmitField('Submit')


class BankInfo(Form):
    StringField("Bank Name", validators=[
        DataRequired(), Length(1, 64), Regexp('^[A-Za-z\s]*$', 0,
                                              'Usernames must have only '
                                              'letters and spaces. '
                                              )])
    FloatField("Account Number",
               validators=[DataRequired(),
                           Length(1, 17, "Please enter an account number."
                                         " It should be between 1 and 17 digits")])
    FloatField("Routing Number",
               validators=[
                   DataRequired(), Length(9, 9, message="Routing numbers "
                                                        "are 9 digits long. "
                                                        "Please check to make "
                                                        "sure you have entered "
                                                        "all 9 digits.")])

    submit = SubmitField('Submit')
