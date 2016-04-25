from flask_wtf import Form
from wtforms import BooleanField, SubmitField, StringField, IntegerField

from wtforms.validators import NumberRange, DataRequired, Length, Regexp

__author__ = 'davidkarapetyan'

act_message = "Account numbers are between 1 and 17 digits long."
route_message = "Routing numbers are 9 digits long. Please enter all 9 digits."


class Invest(Form):
    money = IntegerField('Amount (in $)', validators=[NumberRange(min=0)])
    submit = SubmitField('Submit')


class Liquid(Form):
    is_liquid = BooleanField("Make me liquid.")
    submit = SubmitField('Submit')


class AutoInvest(Form):
    is_liquid = BooleanField("Make me AutoInvest.")
    submit = SubmitField('Submit')


class BankInfo(Form):
    bank = StringField("Bank", validators=[
        DataRequired(), Length(1, 64), Regexp('^[A-Za-z\s]*$', 0,
                                              'Usernames must have only '
                                              'letters and spaces. '
                                              )])
    account_number = StringField("Account Number",
                                 validators=[
                                     DataRequired(), Length(1, 17, act_message),
                                     Regexp('^[0-9]', 0, act_message)])
    routing_number = StringField("Routing Number",
                                 validators=[
                                     DataRequired(),
                                     Length(9, 9, route_message),
                                     Regexp('^[0-9]', 0, route_message)])

    submit = SubmitField('Submit')
