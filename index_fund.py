from flask import redirect, Flask, request, render_template, url_for

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config.from_pyfile('default.cfg')


# @application.route('/signup')
# def signup():
#     return render_template('signup.html', page_title = 'Signup to Bio
# Application')

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
