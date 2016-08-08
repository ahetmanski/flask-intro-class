from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
bootstrap = Bootstrap(app)


class NameForm(Form):
    name = StringField("What is your name?", validators=(DataRequired(), Length(1, 16)))
    submit = SubmitField("Submit")


@app.route("/", methods=("GET", "POST"))
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data.title()
        form.name.data = ""
    return render_template("index.html", form=form, name=name)

if __name__ == "__main__":
    app.secret_key = '\xc2[.Y\xc4\xea]\\Z\xa2)!Z\xc5`\x1c\x1f2\x8c\x15i\xb0}\xee'
    app.run(debug=True)
