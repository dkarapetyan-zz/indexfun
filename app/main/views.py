from flask import render_template, redirect, url_for
from flask.ext.login import login_required, LoginManager

from main.forms import Invest, Liquid, AutoInvest, BankInfo
from . import main

__author__ = 'davidkarapetyan'

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message = "Please log in to access this page."
login_manager.login_message_category = "info"


@main.route('/', methods=["GET", "POST"])
@login_required
def index():
    form = Invest()
    if form.validate_on_submit():
        return redirect(url_for('main.liquid'))
    else:
        return render_template("main/index.html", form=form)


@main.route("/liquid", methods=["GET", "POST"])
@login_required
def liquid():
    form = Liquid()
    if form.validate_on_submit():
        return redirect(url_for("main.bank"))
    else:
        return render_template("main/liquid.html", form=form)


@main.route("/bank", methods=["GET", "POST"])
@login_required
def bank():
    form = BankInfo()
    if form.validate_on_submit():
        return redirect(url_for("main.recurring"))
    else:
        return render_template("main/bank.html", form=form)


@main.route("/recurring", methods=["GET", "POST"])
@login_required
def recurring():
    form = AutoInvest()
    if form.validate_on_submit():
        return redirect(url_for("main.index"))
    else:
        return render_template("main/recurring.html",
                               form=form)
