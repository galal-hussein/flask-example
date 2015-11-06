import os

# default configuration
class BaseConfig(object):
    DEBUG = False
    # Secret key has to be randomly generated
    SECRET_KEY = '\x9a\x80\xce\xa5$[6\xe0\xf2\x01\x1eD{:N"\xdc0$\xc2\xce,/\xf5'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
