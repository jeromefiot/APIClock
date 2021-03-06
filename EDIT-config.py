import os
import logging
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'PUT HERE A SENTENCE HARD TO  GUESS'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    #i use GMAIL so if you want another provider search for good configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'PUT HERE YOUR USERNAME EXP : JEANPAUL@GMAIL.COM'
    MAIL_PASSWORD = 'PUT HERE YOUR MAIL PASSWORD'
    apiclock_MAIL_SUBJECT_PREFIX = 'PUT HERE THE PREFIX YOU WANT TO SEE ON MAIL'
    apiclock_MAIL_SENDER = 'PUT HERE THE SENDER YOU WANT TO DSIPLAY'
    # important !! the user registered with these email will have specials (all) rights !
    apiclock_ADMIN = 'PUT HERE YOUR EMAIL'

    # Logging path
    # This default path should be updated, /tmp/ directory is not safe for logging
    LOGGING_PATH  = "/tmp/apiclock.log"
    # Loging level, by default DEBUG, you may want to use it as NOTICE
    LOGGING_LEVEL = logging.DEBUG

    BASE_APP_DIR  = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'app/')
    UPLOAD_FOLDER = "static/medias/"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'PUT HERE THE NAME OF THE SQLITE DATABASE FOR DEVELOPMENT')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'PUT HERE THE NAME OF THE SQLITE DATABASE FOR TESTING')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'PUT HERE THE NAME OF THE SQLITE DATABASE FOR PRODUCTION')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
