__author__ = 'davidkarapetyan'
from flask_wtf import Form
from wtforms import FloatField

from wtforms.validators import number_range


class Invest(Form):
    money = FloatField('$Amount', validators=number_range(min=0))
