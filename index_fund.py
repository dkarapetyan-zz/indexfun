from flask import redirect, Flask, request, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import Form
import wtforms
from wtforms import StringField, \
    PasswordField, BooleanField
from wtforms.validators import DataRequired
from wtforms.validators import Length, Email


def create_app():
    _app = Flask(__name__, static_folder='static', template_folder='templates')
    _app.config.from_pyfile('default.cfg')
    Bootstrap(_app)
    return _app


app = create_app()


class SignupForm(Form):
    email = StringField('Email address',
                        validators=[
                            DataRequired(
                                'Please provide a valid email address'),
                            Length(min=6, message=u'Email address too short'),
                            Email(
                                message=u'That\'s not a valid email address.')])
    password = PasswordField('Pick a secure password',
                             validators=[
                                 DataRequired(),
                                 Length(min=6,
                                        message='Please give a longer '
                                                'password')])
    username = StringField('Choose your username',
                           validators=[DataRequired()])
    agree = BooleanField('I agree to all the Terms of Services',
                         validators=[
                             DataRequired(
                                 u'You must accept our Terms of Service')])
    submit = wtforms.SubmitField("Submit")


@app.route('/signup', methods=("GET", "POST"))
def signup():
    return render_template('layout.html', form=SignupForm(),
                           page_to_insert="signup.html")


def submit():
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template("signup.html")


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect(url_for("liquid"))
    return render_template("layout.html", page_to_insert="intro.html")


@app.route("/liquid", methods=["GET", "POST"])
def liquid():
    # filled = request.form.getlist("check")
    if request.method == "POST":
        return redirect(url_for("bank"))
    return render_template("layout.html", page_to_insert="liquid.html")


@app.route("/bank", methods=["GET", "POST"])
def bank():
    if request.method == "POST":
        return redirect(url_for("recurring"))
    return render_template("layout.html", page_to_insert="bank.html")


@app.route("/recurring", methods=["GET", "POST"])
def recurring():
    if request.method == "POST":
        return redirect(url_for("index"))
    return render_template("layout.html", page_to_insert="recurring.html")


if __name__ == '__main__':
    app.run(debug=True)
