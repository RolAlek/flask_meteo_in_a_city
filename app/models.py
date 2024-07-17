from flask_login import UserMixin

from . import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    searches = db.relationship("SearchHistory", backref="user", lazy=True)


class SearchHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    count = db.Column(db.Integer, nullable=False)


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
