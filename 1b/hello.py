from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"


@app.route("/user/<name>")
def user(name):
    return "<h4>Hello, {0}!</h4>".format(name.title())


if __name__ == "__main__":
    app.run(debug=True)
