from flask import redirect, request, Flask, render_template, url_for

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect(url_for("liquid"))
    return render_template("layout.html", page_to_insert="intro.html")


@app.route("/liquid", methods=["GET", "POST"])
def liquid():
    return render_template("layout.html", page_to_insert="liquid.html")


if __name__ == '__main__':
    app.run(debug=True)
