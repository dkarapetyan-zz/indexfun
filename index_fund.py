import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    return flask.render_template("layout.html", page_to_insert="about.html")


if __name__ == '__main__':
    app.run(debug=True)
