# import Flask class from the flask module
from project import app, db
from project.models import BlogPost
from flask import  g, redirect, render_template, request, url_for, session, flash, Blueprint
import os
from flask.ext.login import login_required, current_user
from form import MessageForm

################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)

# use decorators to link the function to a url
@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
    error = None
    form = MessageForm(request.form)
    if form.validate_on_submit():
        new_post = BlogPost(
            form.title.data,
            form.description.data,
            current_user.id
        )
        db.session.add(new_post)
        db.session.commit()
        flash('New post was added, thanks.')
        return redirect(url_for('home.home'))
    else:
        posts = db.session.query(BlogPost).filter_by(author_id=current_user.id).all()
        return render_template('index.html', posts=posts, form=form, error=error)

# another decorators
@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')
