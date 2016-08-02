from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    return render_template("index.html", months=months, city="Minsk")

if __name__ == "__main__":
    app.run(debug=True)
