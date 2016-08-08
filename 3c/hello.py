from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
app = Flask(__name__)
bootstrap = Bootstrap(app)


class CustomForm(Form):
    name = StringField("What is your name?", (DataRequired(), Length(1, 16)))
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    form = CustomForm()
    if form.validate_on_submit():
        name = form.name.data.title()
        form.name.data = ""
    return render_template("index.html", form=form, name=name)

if __name__ == "__main__":
    app.secret_key = "ksjdfsjkaas;d;"
    app.run(debug=True)
