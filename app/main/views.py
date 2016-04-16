from flask import render_template, redirect, url_for, request
from flask.ext.login import login_required, LoginManager

from . import main

__author__ = 'davidkarapetyan'

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message = "Please log in to access this page."
login_manager.login_message_category = "info"


@main.route('/', methods=["GET", "POST"])
@login_required
def index():
    return render_template('layout.html', page_to_insert="index.html")


@main.route("/liquid", methods=["GET", "POST"])
@login_required
def liquid():
    # filled = request.form.getlist("check")
    if request.method == "POST":
        return redirect(url_for("main.bank"))
    return render_template("layout.html", page_to_insert="liquid.html")


@main.route("/bank", methods=["GET", "POST"])
@login_required
def bank():
    if request.method == "POST":
        return redirect(url_for("main.recurring"))
    return render_template("layout.html", page_to_insert="bank.html")


@main.route("/recurring", methods=["GET", "POST"])
@login_required
def recurring():
    if request.method == "POST":
        return redirect(url_for("main.index"))
    return render_template("layout.html", page_to_insert="recurring.html")
