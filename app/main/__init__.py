__author__ = 'davidkarapetyan'

from flask import Blueprint

main = Blueprint('main', __name__)
from . import views, errors
