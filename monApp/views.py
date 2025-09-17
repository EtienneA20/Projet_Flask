from .app import app
from config import ABOUT,CONTACT
from flask import render_template

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html",title ="R3.01 Dev Web avec Flask",name="Cricri")

@app.route("/about")
def about():
    return render_template("about.html",title ="R3.01 Dev Web avec Flask",var=ABOUT)


@app.route("/contact")
def contact():
    return render_template("contact.html",title ="R3.01 Dev Web avec Flask",var=CONTACT)


if __name__ == "__main__":
    app.run()