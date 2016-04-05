__author__ = 'davidkarapetyan'

from flask import Blueprint

auth = Blueprint('auth', __name__)
from . import views
