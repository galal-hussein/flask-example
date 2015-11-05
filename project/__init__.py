# import Flas class from the flask module
from flask import Flask
import os
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager

# create the application object
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
# create the sqlalchemy object
login_manager = LoginManager()

login_manager.init_app(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from project.users.views import users_blueprint
from project.home.views import home_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)

from models import User

login_manager.login_view = "users.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
