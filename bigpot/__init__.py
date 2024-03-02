import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa



app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

app.config["SECRET_KEY"] = '123d3d3'#os.environ.get("SECRET_KEY")
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
SQLALCHEMY_DATABASE_URI = 'sqlite:///mylocaldb.db'  # SQLite database named mylocaldb.db in the same directory as your app
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)

from bigpot import routes  # noqa