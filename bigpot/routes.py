import os
import json
from bigpot import app
from flask import render_template, session, redirect, request, flash, url_for

comments = []

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

    return render_template("community.html", page_title='Community', comments=comments)

@app.route('/submit-comment', methods=['POST'])
def submit_comment():
    name = request.form['name']
    comment = request.form['comment']
    comments.append({'name': name, 'comment': comment})
    return redirect(url_for('community'))

@app.route('/edit-comment', methods=['POST'])
def edit_comment():
    comment_id = int(request.form['comment_id'])
    edited_comment = request.form['edited_comment']
    comments[comment_id - 1]['comment'] = edited_comment
    return redirect(url_for('community'))

@app.route('/delete-comment', methods=['POST'])
def delete_comment():
    comment_id = int(request.form['comment_id'])
    del comments[comment_id - 1]
    return redirect(url_for('community'))
