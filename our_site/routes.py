from our_site import the_site, db
from our_site.forms import TimeInserted, Shuffling, FlashCards, RegistrationForm, LoginForm
from our_site.models import FlashCard, User
import time
import datetime
import random
from flask import escape, flash, render_template, redirect, request
from flask_login import current_user, login_required, login_user, logout_user

@the_site.route('/', methods=['GET', 'POST'])
def home():
    form = RegistrationForm()
    print('before')
    # if form.validate_on_submit():
    if request.method == 'POST':
        print('bs class')
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user is None:
            new_user = User(
                username = form.username.data
            )
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect('/menu')
        flash('Usernames must be unique!')
    print('no')
    return render_template('home.html', form=form)

@the_site.route('/timer/<string:t>/')
def timer(t):
	if ':' in t:
		timeInput = t.split(':')
		hour = int(timeInput[0])
		minute = int(timeInput[1])
		second = int(timeInput[2])
		if minute > 59 or second > 59:
			return render_template('invalidTime.html')
		# https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html
		totalSeconds = hour * 3600 + minute * 60 + second
		time.sleep(totalSeconds)
		timeSpent = str(hour) + ' hour(s), ' + str(minute) + ' minute(s), and ' + str(second) + ' second(s) has/have passed!'
		return render_template('timer.html', timeSpent=timeSpent)
	else:
		return render_template('invalidTime.html')

@the_site.route('/thetimer', methods=['GET', 'POST'])
def thetimer():
	form = TimeInserted()
	if form.validate_on_submit():
		theLink = '/timer/' + form.inserted_time.data + '/'
		return redirect(theLink)
	return render_template('thetimer.html', form=form)

@the_site.route('/overview', methods=['GET', 'POST'])
def overview():
	form = Shuffling()
	# https://www.w3schools.com/HTML/html_lists.asp
	# all_cards = FlashCard.query.all()
	all_cards = []
	for card in current_user.cardsofuser:
		all_cards.append(card)
	if form.validate_on_submit():
		flash('Cards have been shuffled!')
		# https://www.w3schools.com/python/ref_random_shuffle.asp
		random.shuffle(all_cards)
	return render_template('overview.html', all_cards=all_cards, form=form)

@the_site.route('/createcards', methods=['GET', 'POST'])
def createcards():
	form = FlashCards()
	if form.validate_on_submit():
		flash('Flashcard added!')
		card = FlashCard(card_term = form.card_term.data, card_def = form.card_def.data)
		db.session.add(card)
		db.session.commit()
		# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
		# https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-many
		# https://www.youtube.com/watch?v=OvhoYbjtiKc
		# Links I used to help make many to many relationships
		# https://www.codegrepper.com/code-examples/python/how+to+check+if+user+is+logged+in+flask
		if current_user.is_authenticated == True:
			card.Users.append(current_user)
			db.session.commit()
		return redirect('/createcards')
	return render_template('entercard.html', form=form)

@the_site.route('/menu')
@login_required
def menu():
    return render_template('menu.html')

@the_site.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            return redirect('/menu')
        flash('Wrong username and/or password!')
    return render_template('login.html', form=form)

@the_site.route("/logout")
def logout():
    logout_user()
    flash('User logged out')
    return redirect('/')

