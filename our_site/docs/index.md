# Welcome to BetterStudent

The ultimate school assistant. Includes features for note-taking and memorization.

# Installation

## Prerequisites

You need to have Python3 installed on your machine. If you do not, follow [these
instructions](https://realpython.com/installing-python/) to install.

## Cloning the Repository

To clone the repository, copy and paste the following into your terminal:
```
git clone https://github.com/Jgoody4/Team-5.git
cd Team-5
```

### Installing Libraries

While still in the `Team-5` directory, copy and paste the following into your
terminal:
```
pip install flask flask-wtf flask-login
```
This installs the three libraries necessary for functioning (and logins).

# Usage
To run the program, in the `Team-5` directory, copy and paste the following
into your terminal:
```
py run.py
```
If this gives errors, you can replace this with `python3 run.py` or `python run.py`.

In a second terminal, copy and paste the following into your terminal:
```py
py
from our_site import db
from our_site.models import *
db.create_all()
```
Finally, navigate to [`localhost:5000`](localhost:5000) and you will see the
project!

Notice that most functionalities require a user to be logged in. The first page
is a registration page for this very reason.

## Project Directory

```
Team-5
│   .gitignore
│   README.md
│   run.py
│   Specification.md
│   test.txt
│
└───our_site
    │   .DS_Store
    │   app.db
    │   forms.py
    │   mkdocs.yml
    │   models.py
    │   routes.py
    │   __init__.py
    │
    ├───docs
    │       forms.md
    │       index.md
    │       models.md
    │       routes.md
    │
    ├───templates
    │       .DS_Store
    │       entercard.html
    │       folder.html
    │       graph.html
    │       highlight.html
    │       home.html
    │       invalidTime.html
    │       login.html
    │       markdown.html
    │       match.html
    │       menu.html
    │       overview.html
    │       reminder.html
    │       thetimer.html
    │       timer.html
    │
    └───__pycache__
            forms.cpython-38.pyc
            models.cpython-38.pyc
            routes.cpython-38.pyc
            __init__.cpython-38.pyc
```