from flask import flash, redirect
from flask_login import UserMixin
from our_site import db, login
from werkzeug.security import check_password_hash, generate_password_hash

cards = db.Table('cards',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('flashcard_id', db.Integer, db.ForeignKey('flashcard.id'), primary_key=True)
)

class FlashCard(db.Model):
    __tablename__ = 'flashcard'
    id = db.Column(db.Integer, primary_key=True)
    card_term = db.Column(db.String(64), index=True, unique=True)
    card_def = db.Column(db.String(128), index=True, unique=True)

    def __repr__(self):
        return f'Term: {self.card_term}, Definition: {self.card_def}'


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    password_hash = db.Column(db.String(256))

    def __repr__(self):
        return {self.id, self.username, self.password_hash}

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='sha256')

    cardsofuser = db.relationship('FlashCard', secondary=cards, lazy='subquery', backref=db.backref('Users', lazy=True))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@login.unauthorized_handler
def unauthorized():
    flash('You aren\'t authorized to go there!')
    return redirect('/login')
