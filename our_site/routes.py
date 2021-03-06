from our_site import the_site, db, mail
from our_site.forms import *
from our_site.models import *
import time as TIME
from datetime import *
import random
from flask import escape, flash, render_template, redirect, request
from flask_login import current_user, login_required, login_user, logout_user
from flask_mail import Message


@the_site.route('/', methods=['GET', 'POST'])
def splash():
    return render_template('splash.html')


@the_site.route('/registration', methods=['GET', 'POST'])
def home():
    '''
    Function that implements registration of users.

        Returns:
            render_template(str, form): Page that shows a form to register users
            with unique username and password and a link to the login page.
            redirect(str, <form>): Redirects user to a specific page. If the
            <form> object was included, also returns the registration form.
    '''
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Checks if a specific username is taken already
            existing_user = User.query.filter_by(
                username=form.username.data).first()
            if existing_user is None:
                new_user = User(
                    username=form.username.data
                )
                new_user.set_password(form.password.data)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                return redirect('/menu')
            flash('Usernames must be unique!')
    flash(form.errors)
    return render_template('home.html', form=form)


@the_site.route('/timer/<string:t>/')
def timer(t):
    '''
    Function works as a working timer, returns a page that displays the amount of time passed.

        Parameters:
            t (str): A string in the form of 00:00:00

        Returns:
            render_template (str, timeSpent): Page that either shows the amount of time that
            had passed or an error page
    '''
    # Following code only works if t is in the form of 00:00:00, if not then error.
    if ':' in t:
        # Splits the string into hours, minutes, and seconds.
        timeInput = t.split(':')
        hour = int(timeInput[0])
        minute = int(timeInput[1])
        second = int(timeInput[2])
        # If the minute and second was more than 59, then it is an error.
        if minute > 59 or second > 59:
            return render_template('invalidTime.html')
        # Convert the string into its total seconds, then freezes the code's run for that time.
        '''
        Title: Create a Timer in Python: Step-by-Step Guide
        Author: Udacity Team
        Date: 2021
        Availability: https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html
        '''
        totalSeconds = hour * 3600 + minute * 60 + second
        TIME.sleep(totalSeconds)
        # Creates string that contains the amount of time that had passed.
        timeSpent = str(hour) + ' hour(s), ' + str(minute) + \
            ' minute(s), and ' + str(second) + ' second(s) has/have passed!'
        return render_template('timer.html', timeSpent=timeSpent)
    else:
        return render_template('invalidTime.html')


@the_site.route('/thetimer', methods=['GET', 'POST'])
def thetimer():
    '''
    Returns a page that asks user to enter an amount of time.

        Returns:
            render_template (str, form): Page that asks user to enter an amount of time with a textbox
            redirect (theLink): If the user submits the time, they will be redirected to the page that
            displays the amount of time that had passed
    '''
    form = TimeInserted()
    # If the submit button was clicked, the user will be redirected to the page that displays the time passed.
    if form.validate_on_submit():
        theLink = '/timer/' + form.inserted_time.data + '/'
        return redirect(theLink)
    return render_template('thetimer.html', form=form)

#Justin
@the_site.route('/totalTimeStudied', methods=['GET', 'POST'])
def totalTimeStudied():
    return render_template('totalTimeStudied.html')

@the_site.route('/overheadview', methods=['GET', 'POST'])
def overheadview():
    '''
    Returns a page that works as a overhead view page of the user's flashcards.

        Returns:
            render_template (str, all_cards, form): Page that prints all the user's flashcards in a
            single page, as well as a shuffle button that shuffles the order.
    '''
    form = Shuffling()
    all_cards = []
    # The user's flashcards are inserted into the all_cards list.
    for card in current_user.cardsofuser:
        all_cards.append(card)
    # If the user clicks the shuffle button, the order of the flashcards in the page will be shuffled.
    if form.validate_on_submit():
        flash('Cards have been shuffled!')
        '''
        Title: Python Random shuffle() Method
        Author: w3schools
        Date: 2021
        Availability: https://www.w3schools.com/python/ref_random_shuffle.asp
        '''
        random.shuffle(all_cards)
    return render_template('overview.html', all_cards=all_cards, form=form)


@the_site.route('/createcards', methods=['GET', 'POST'])
def createcards():
    '''
    Returns a page that allows the user to create their own flashcards.

        Returns:
            render_template (str, form): Page that asks the user to insert a term and definition in
            textboxes to create a flashcard, and a button that submits the flashcard into the database
            redirect (str): Redirects user back to this page
    '''
    form = FlashCards()
    # If the user hits submit, the flashcard will be made and added to the database.
    if form.validate_on_submit():
        flash('Flashcard added!')
        card = FlashCard(card_term=form.card_term.data,
                         card_def=form.card_def.data)
        db.session.add(card)
        db.session.commit()
        # If the user is signed in, the card will belong to the user.
        '''
        Title: Creating Many-To-Many Relationships in Flask-SQLAlchemy
        Author: Pretty Printed
        Date: 2016
        Availability: https://www.youtube.com/watch?v=OvhoYbjtiKc
        '''
        '''
        Title: Grepper
        Author: Sistrometic
        Date: 2020
        Availability: https://www.codegrepper.com/code-examples/python/how+to+check+if+user+is+logged+in+flask
        '''
        if current_user.is_authenticated == True:
            card.Users.append(current_user)
            db.session.commit()
        return redirect('/createcards')
    return render_template('entercard.html', form=form)


@the_site.route('/reminder', methods=['GET', 'POST'])
def reminder():
    '''
    Returns a page that shows the reminders the user has set up.

        Returns: 
            render_template (str, form): The page have the user enter a task to set
            reminder for and the time for the reminder and a submit button which 
            will display the reminder
    '''
    form = Reminder()
    if form.validate_on_submit():
        flash(
            f'Reminder to do: {form.reminder_task.data} at {form.reminder_time.data}')
    return render_template('reminder.html', form=form)


@the_site.route('/match', methods=['GET', 'POST'])
def match():
    '''
    Returns a page that tests the memorization of the user

        Returns: 
            render_template (str, form): Page shuffles the card and adds the cards' term
            and definition to each respective list. Then the page will record the number 
            of right or wrong based on text input into the form.
            redirect (str): Redirects the user to a performance graph after going through
            all the cards
    '''
    form = Match()
    all_cards = FlashCard.query.all()
    questionList = []
    answerList = []
    right = 0
    wrong = 0

    random.shuffle(all_cards)

    for card in all_cards:
        questionList.append(card.card_term)

    for card in all_cards:
        answerList.append(card.card_def)

    if form.validate_on_submit():
        current_card_index = 0
        while current_card_index <= len(questionList):
            if form.answer.data == questionList[current_card_index]:
                right += 1
            else:
                wrong += 1

            current_card_index + 1

        right_total = right/len(questionList)
        wrong_total = wrong/len(questionList)

        return redirect("/results", right_total=right_total, wrong_total=wrong_total)
    return render_template('match.html', form=form, questionList=questionList)


@the_site.route('/results', methods=['GET', 'POST'])
def analytic():
    '''
    Returns a graph for the user to see their memorization performance

        Return:
            render_template(str): Shows a page of the graph
    '''
    return render_template('graph.html')


@the_site.route('/markdown', methods=['GET', 'POST'])
def markdown():
    '''
    Returns a page of the html version of the markdown notes

        Return:
            render_template(str): Shows the markdown notes the user had typed
    '''
    form = Markdown()

    return render_template('markdown.html', form=form)


@the_site.route('/schedule', methods=['GET', 'POST'])
@login_required
def schedule():
    form = DateForm()
    if request.method == 'POST':
        print(form.validate_on_submit())
        if form.validate_on_submit():
            start = datetime.strptime(f'{form.start_date.data}',
                                                     '%Y-%m-%d %H:%M:%S')
            end = datetime.strptime(f'{form.end_date.data}',
                                                   '%Y-%m-%d %H:%M:%S')
            flash(f'Event {form.name.data} created!')
            event = Dates(
                name=form.name.data,
                start_datetime=form.start_date.data,
                end_datetime=form.end_date.data
            )
            db.session.add(event)
            db.session.commit()
            return redirect('/menu')
        flash('Enter the date in the correct format!')
    flash(form.errors)
    return render_template('schedule.html', form=form)


@the_site.route('/share', methods=['GET', 'POST'])
def share():
    form = MailingForm()
    if request.method == 'POST':
        try:
            email = str(request.form['email'])
            subject = str(request.form['subject'])
            msg_body = 'I\'m sending you these notes!'
            message = Message(
                subject,
                sender='teamfive131s02@gmail.com',
                recipients=[email]
            )
            message.body = msg_body
            message.attach(
                form.file.data.filename,
                'application/octect-stream',
                form.file.data.read()
            )
            mail.send(message)
            flash('Notes sent!')
            return redirect('/menu')
        except ConnectionRefusedError as connectionRefusedError_:
            return 'Didn\'t send email. Try again later.'
    else:
        return render_template('share.html', form=form)


@the_site.route('/menu')
@login_required
def menu():
    '''
    Function that shows the menu page with all the links to the various services.

    Returns:
        render_template(str): Page with links to all services and a logout option.
    '''
    return render_template('menu.html')


@the_site.route("/login", methods=['GET', 'POST'])
def login():
    '''
    Function that shows the login page with a link to register user.

    Returns:
        render_template(str, form): Page that shows a form that takes a username
        and password to login a user.
        redirect(str): Redirects the user to the menu page.
    '''
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
    '''
    Function that logs out a user.

    Returns:
        redirect(str): Redirects a user to the registration page.
    '''
    logout_user()
    flash('User logged out')
    return redirect('/')
