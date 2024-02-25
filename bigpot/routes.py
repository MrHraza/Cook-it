import os
import json
from bigpot import app, db
from flask import render_template, session, redirect, request, flash, url_for


@app.route("/")
def index():
    data = []
    with open("data/recipies.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("index.html", recipies=data)

@app.route("/about")
def about():
    return render_template("about.html", page_title='About Us')

@app.route("/contact")
def contact():
    return render_template("contact.html", page_title='Contact Us')

@app.route("/community")
def community():
    return render_template("community.html", page_title='Community')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Replace the following line with your user authentication logic
        if username == "admin" and password == "secret":
            session['logged_in'] = True
            return redirect(url_for("index"))
        else:
            flash("Invalid credentials", "danger")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    return redirect(url_for("index"))