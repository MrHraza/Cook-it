import os
import json
from bigpot import app, db
from flask import render_template, session, redirect, request, flash, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from bigpot.models import Users, Comments


@app.route("/")
def index():
    data = []
    with open("data/recipies.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("index.html", recipies=data)

#about page

@app.route("/about")
def about():
    return render_template("about.html", page_title='About Us')

#Contact page

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thank you, we have received your message. A member of our team will reach out to you within 24 hours.")
    return render_template("contact.html", page_title='Contact Us')

# community page

@app.route("/community")
def community():
    comments = Comments.query.join(Users).all()
    return render_template("community.html", page_title='Community', comments=comments)

# login/logout

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
                session['logged_in'] = True
                return redirect(url_for('index'))
            else:
                flash('Incorrect password. Try again.', 'error')
                return redirect(url_for('login'))
        else:
            flash('User not found. Please try again.', 'error')
            return redirect(url_for('login'))

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop('logged_in', None)
    session.clear()
    return redirect(url_for("index"))

#sign up page

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
        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred: {str(e)}", "error")

    return render_template("signup.html")

#community functions

@app.route("/add_comment", methods=["POST"])
def add_comment():
    if 'user_id' not in session:
        flash('Please log in to add a comment.', 'error')
        return redirect(url_for('login'))

    user_id = session['user_id']

    comment_text = request.form.get('comment')

    new_comment = Comments(user_id=user_id, comment=comment_text)
    db.session.add(new_comment)
    db.session.commit()

    flash('Comment added successfully!', 'success')
    return redirect(url_for('community'))

@app.route("/delete_comment/<int:comment_id>", methods=["POST"])
def delete_comment(comment_id):
    comment = Comments.query.get(comment_id)

    if not comment:
        flash("Comment not found.", "error")
        return redirect(url_for("community"))

    try:
        db.session.delete(comment)
        db.session.commit()
        flash("Comment deleted successfully.", "success")
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")

    return redirect(url_for("community"))

@app.route("/edit_comment/<int:comment_id>", methods=["GET", "POST"])
def edit_comment(comment_id):
    comment = Comments.query.get(comment_id)
    if not comment:
        flash("Comment not found.", "error")
        return redirect(url_for("community"))

    if session.get("user_id") != comment.user_id:
        flash("You can only edit your own comments.", "error")
        return redirect(url_for("community"))

    if request.method == "POST":
        new_comment_text = request.form.get("new_comment_text")
        if new_comment_text:
            comment.comment = new_comment_text
            db.session.commit()
            flash("Comment updated successfully.", "success")
            return redirect(url_for("community"))

    return render_template("edit_comment.html", comment=comment)