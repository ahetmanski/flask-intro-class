from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"


@app.route("/another")
def another():
    return "<h6>Another small string</h6>"


if __name__ == "__main__":
    app.run(host="192.168.56.101", port=1234, debug=True)
