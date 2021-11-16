from our_site import the_site
from flask import render_template


@the_site.route('/')
def home():
    return render_template('home.html')
