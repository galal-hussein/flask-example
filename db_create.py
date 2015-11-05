from app import db
from models import BlogPost, User

#create the database and db tables

#insert
#db.session.add(BlogPost("Good", "I\'m good."))
#db.session.add(BlogPost("Well", "I\'m well."))
#db.session.add(BlogPost("Postgres", "It Worked!"))
db.session.add(User("Postgres", "It Worked!"))
#commit changes

db.session.commit()
