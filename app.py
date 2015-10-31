# import Flask class from the flask module
from flask import Flask, g, redirect, render_template, request, url_for, session, flash
from functools import wraps
import os
#import sqlite3

from flask.ext.sqlalchemy import SQLAlchemy
# create the application object
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print os.environ['APP_SETTINGS']
# create the sqlalchemy object
db = SQLAlchemy(app)

from models import *

# Login required decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap

# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    #return "Hello, World!"
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)

# another decorators
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = "Invalid credentials"
        else:
            session['logged_in'] = True
            flash('You logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You logged out!')
    return redirect(url_for('welcome'))

# start the server
if __name__ == '__main__':
    app.run(port=5555)
