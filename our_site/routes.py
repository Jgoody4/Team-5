from flask import escape, flash, render_template, redirect
from flask_login import login_required, login_user, logout_user
from our_site import the_site
from our_site import db
from our_site.forms import RegistrationForm
from our_site.models import User


@the_site.route('/', methods=['GET', 'POST'])
def home():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            redirect('/')
        login_user(user, remember=form.remember_me.data)
        return redirect('/menu')
    return render_template('home.html', form=form)

@the_site.route('/menu')
@login_required
def menu():
    return '1'

@the_site.route("/logout")
def logout():
    logout_user()
    flash('User logged out')
    return redirect('/')