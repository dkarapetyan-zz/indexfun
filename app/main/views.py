__author__ = 'davidkarapetyan'
from flask import render_template, redirect, url_for, request

from . import main
from .forms import SignupForm


@main.route('/signup', methods=("GET", "POST"))
def signup():
    if request.method == "POST":
        form = request.form
        if form.validate_on_submit():
            return redirect(url_for("main.info"))
    return render_template('layout.html', form=SignupForm(),
                           page_to_insert="signup.html")


@main.route('/', methods=["GET", "POST"])
def index():
    return redirect(url_for("main.signup"))


@main.route("/liquid", methods=["GET", "POST"])
def liquid():
    # filled = request.form.getlist("check")
    if request.method == "POST":
        return redirect(url_for("main.bank"))
    return render_template("layout.html", page_to_insert="liquid.html")


@main.route("/bank", methods=["GET", "POST"])
def bank():
    if request.method == "POST":
        return redirect(url_for("main.recurring"))
    return render_template("layout.html", page_to_insert="bank.html")


@main.route("/recurring", methods=["GET", "POST"])
def recurring():
    if request.method == "POST":
        return redirect(url_for("main.index"))
    return render_template("layout.html", page_to_insert="recurring.html")
