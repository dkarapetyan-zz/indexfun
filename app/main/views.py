from flask import render_template, redirect, url_for, request

from . import main

__author__ = 'davidkarapetyan'


@main.route('/', methods=["GET", "POST"])
def index():
    return render_template('layout.html', page_to_insert="index.html")


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
