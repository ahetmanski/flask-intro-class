import os
import imghdr
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import SubmitField, FileField, ValidationError
app = Flask(__name__)
bootstrap = Bootstrap(app)


class UploadForm(Form):
    image_file = FileField("Upload file")
    submit = SubmitField("Submit")

    def validate_image_file(self, field):
        if field.data.filename[-4:].lower() != ".jpg":
            raise ValidationError("Passed file should have 'jpg' extension only.")
        if imghdr.what(field.data) != "jpeg":
            raise ValidationError("Passed file should be in 'jpeg' format.")


@app.route("/", methods=("GET", "POST"))
def index():
    filename = None
    form = UploadForm()
    if form.validate_on_submit():
        filename = os.path.join("uploads", form.image_file.data.filename)
        form.image_file.data.save(os.path.join(app.static_folder, filename))
    return render_template("index.html", form=form, filename=filename)

if __name__ == "__main__":
    app.secret_key = "secret KEY"
    app.run(debug=True)
