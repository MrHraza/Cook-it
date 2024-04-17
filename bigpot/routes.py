import os
import json
from bigpot import app, db
from flask import render_template, session, redirect, request, flash, url_for
from bigpot.models import Users, Comments




@app.route("/")
def index():
    data = []
    with open("data/recipies.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("index.html", recipies=data)

@app.route("/about")
def about():
    return render_template("about.html", page_title='About Us')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thank you, we have received your message. A member of our team will reach out to you within 24 hours.")
    return render_template("contact.html", page_title='Contact Us')

@app.route("/community")
def community():
    return render_template("community.html", page_title='Community')

@app.route("/login")
def login():
    return render_template("login.html", page_title='Login')

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/add_user", methods=["GET", "POST"])
def add_users():
    if request.method == "POST":
        user = Users(username=request.form.get("username"))
        password = Users(password=request.form.get("password"))
        email = Users(email=request.form.get("email"))
        db.session.add(user)
        db.session.add(password)
        db.session.add(email)
        db.session.commit()
        return redirect("{{ url_for('login') }}")
    return render_template("signup.html")