from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    return render_template("index.html", city="Minsk, BY")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", error=error), 404

if __name__ == "__main__":
    app.run(debug=True)
