from flask import flash, redirect
from flask_login import UserMixin
from our_site import db, login
from werkzeug.security import check_password_hash, generate_password_hash
import time

# Creates a table in order to create a successful many to many relationship.
'''
Title: Declaring Models
Author: Pallets
Date: 2010
Availability: https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
'''
cards = db.Table('cards',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('flashcard_id', db.Integer, db.ForeignKey('flashcard.id'), primary_key=True)
)

class FlashCard(db.Model):
    # Overriding the table name.
    __tablename__ = 'flashcard'
    # The flashcard model for the database, which contains the card's id, term and definition.
    id = db.Column(db.Integer, primary_key=True)
    card_term = db.Column(db.String(64), index=True, unique=True)
    card_def = db.Column(db.String(128), index=True, unique=True)

    def __repr__(self):
        '''
        Returns a string that represents a specific card's term and definition.
        '''
        return f'Term: {self.card_term}, Definition: {self.card_def}'


class User(UserMixin, db.Model):
    # Overriding the table name.
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

    # Creates a relationship between users and flashcards.
    cardsofuser = db.relationship('FlashCard', secondary=cards, lazy='subquery', backref=db.backref('Users', lazy=True))

#This class is used for a running timer for total time studied
class Stopwatch():
    def time_convert(sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        print("Time studied = {0}:{1}:{2}".format(int(hours), int(mins),sec))
        #Here needs to be when user opens /stopwatch or /overheadview then start timer
        start_time = time.time()
        #Here is when the user leaves the page the stopwatch ends
        end_time = time.time()
        time_studied = end_time - start_time
        time_convert(time_studied)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@login.unauthorized_handler
def unauthorized():
    flash('You aren\'t authorized to go there!')
    return redirect('/login')
