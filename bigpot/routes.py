from flask import render_template
from bigpot import app, db


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html", page_title='About')

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/community")
def community():
    return render_template("community.html")