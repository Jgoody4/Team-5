from flask import Flask
import os
basedir = os.path.abspath(os.path.dirname(__file__))
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

the_site = Flask(__name__)
Bootstrap(the_site)

the_site.config.from_mapping(
    SECRET_KEY = 'you-will-know',
    # location of sqlite database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
)

db = SQLAlchemy(the_site)
with the_site.app_context():
    db.create_all()

login = LoginManager(the_site)
# right side is the function that's called to login users
login.login_view ='login'
from our_site import routes, models
