import os
import json
from bigpot import app, db
from flask import render_template, session, redirect, request, flash, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.exc import IntegrityError
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
    comments = Comments.query.all()
    return render_template("community.html", page_title='Community')

@app.route("/login")
def login():
    return render_template("login.html")    

@app.route('/login', methods=['POST'])
def authentication():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    
        user = Users.query.filter_by(username=username).first()
        
        if user:
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                return redirect(url_for('index'))
            else:
                flash('Incorrect password. Please try again.', 'error')
                return redirect(url_for('login'))
        else:
            flash('User not found. Please try again.', 'error')
            return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    return redirect(url_for("index"))

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/add_user", methods=["GET", "POST"])
def add_users():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        hashed_password = generate_password_hash(password)

        new_user = Users(username=username, password=hashed_password, email=email)

        db.session.add(new_user)

        try:
            db.session.commit()
            flash("User created successfully!", "success")
            return redirect(url_for("login"))
        except IntegrityError as e:
            db.session.rollback()
            error_message = str(e.orig)
            flash(f"An error occurred: {error_message}", "error")

    return render_template("signup.html")

@app.route('/add_comment', methods=['POST'])
def add_comment():

    if not current_user :
        return redirect(url_for('login'))

    comment_text = request.form['comment']

    new_comment = Comments(user_id=current_user.id, comment=comment_text)
    db.session.add(new_comment)
    db.session.commit()

    return redirect(url_for('community'))

    