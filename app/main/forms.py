__author__ = 'davidkarapetyan'
from flask_wtf import Form
from wtforms import FloatField, BooleanField, SubmitField

from wtforms.validators import number_range


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
    submit = SubmitField('Submit')
