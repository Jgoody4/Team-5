from our_site import the_site, db
from flask import render_template, redirect
from our_site.forms import TimeInserted
from our_site.models import FlashCard
import time
import datetime

@the_site.route('/')
def home():
    return render_template('home.html')

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

@the_site.route('/overview')
def overview():
	# https://www.w3schools.com/HTML/html_lists.asp
	all_cards = FlashCard.query.all()
	return render_template('overview.html', all_cards=all_cards)
