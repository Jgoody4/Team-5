from our_site import the_site
from flask import render_template
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
