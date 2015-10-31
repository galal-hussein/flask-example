# import Flask class from the flask module
from flask import Flask, g, redirect, render_template, request, url_for, session, flash
from functools import wraps
import sqlite3

# create the application object
app = Flask(__name__)

app.secret_key = 'mysecretkey'
app.database = "sample.db"


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
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    g.db.close()
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

def connect_db():
    return sqlite3.connect(app.database)

# start the server
if __name__ == '__main__':
    app.run(debug=True, port=5555)
