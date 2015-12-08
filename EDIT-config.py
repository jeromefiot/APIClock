import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'PUT HERE A SENTENCE HARD TO  GUESS'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    #i use GMAIL so if you want another provider search for good configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'benoit.heraud@gmail.com'
    MAIL_PASSWORD = 'calamari1'
    apiclock_MAIL_SUBJECT_PREFIX = 'PUT HERE THE PREFIX YOU WANT TO SEE ON MAIL'
    apiclock_MAIL_SENDER = 'PUT HERE THE SENDER YOU WANT TO DSIPLAY'
    # important !! the user registered with these email will have specials (all) rights !
    apiclock_ADMIN = 'benoit.heraud@gmail.com'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'devdb.db')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'testdb.db')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'proddb.db')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
