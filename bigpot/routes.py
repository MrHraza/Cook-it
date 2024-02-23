import os
import json
from flask import render_template
from bigpot import app, db


@app.route("/")
def index():
    data = []
    with open("data/recipies.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("index.html", recipies=data)

@app.route("/about")
def about():
    return render_template("about.html", page_title='About')

@app.route("/contact")
def contact():
    return render_template("contact.html", page_title='Contact')

@app.route("/community")
def community():
    return render_template("community.html", page_title='Community')