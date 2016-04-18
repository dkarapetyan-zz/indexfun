__author__ = 'davidkarapetyan'
from flask_wtf import Form
from wtforms import FloatField, BooleanField

from wtforms.validators import number_range


class Invest(Form):
    money = FloatField('$Amount', validators=number_range(min=0))


class Liquid(Form):
    is_liquid = BooleanField("Make me liquid.")


class AutoInvest(Form):
    is_liquid = BooleanField("Make me AutoInvest.")
