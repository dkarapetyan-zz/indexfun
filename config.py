import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    WTF_CSRF_ENABLED = True
    WTF_SECRET_KEY = "7136d81446d5caabe16ac77cd41df5d3"
    SECRET_KEY = "7136d81446d5caabe16ac77cd41df5d3"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = "indexfund1@gmail.com"
    MAIL_PASSWORD = "rainbow!#"
    DEV_DATABASE_URI = "postgres://postgres@localhost/index_fund"
    INDEX_FUND_MAIL_SUBJECT_PREFIX = '[Index Fund]'
    INDEX_FUND_MAIL_SENDER = 'David Karapetyan <indexfund1@gmail.com>'
    INDEX_FUND_ADMIN = "David Karapetyan"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,
                                                            'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir,
                                                          'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
