import os

# default configuration
class BaseConfig(object):
    DEBUG = False
    # Secret key has to be randomly generated
    SECRET_KEY = '\x9a\x80\xce\xa5$[6\xe0\xf2\x01\x1eD{:N"\xdc0$\xc2\xce,/\xf5'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
