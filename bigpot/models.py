from bigpot import db
from datetime import datetime

class Users(db.Model):
   
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    
    def __repr__(self):
        return self.username

class Comments(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = db.relationship("Users", backref="comments")

    def __repr__(self):
        return "#{0} | User Id: {1} | Comment: {2} | Date posted: {3} | Date updated: {4}".format(self.id, self.user_id, self.comment, self.date_posted, self.date_updated)

