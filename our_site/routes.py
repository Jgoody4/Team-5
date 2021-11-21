from flask import escape, flash, render_template, redirect
from flask_login import current_user, login_required, login_user, logout_user
from our_site import the_site
from our_site import db
from our_site.forms import RegistrationForm
from our_site.models import User


@the_site.route('/', methods=['GET', 'POST'])
def home():
    form = RegistrationForm()
    if form.validate_on_submit():
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