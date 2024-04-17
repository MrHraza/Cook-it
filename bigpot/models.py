from bigpot import db


class Users(db.Model):
    # schema for the users model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    #comment = db.relationship("comments", backref="users", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.username

class Comments(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.Date)
    date_updated = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} | User Id: {1} | Comment: {2} | Date posted: {3} | Date updated: {4}".format(self.id, self.user_id, self.comment, self.date_posted, self.date_updated)

