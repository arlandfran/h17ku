import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    """Base configuration class."""

    TESTING = False
    SECRET_KEY = os.environ["SECRET_KEY"]
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Strict"


class DevConfig(Config):
    MONGO_URI = os.environ["DEV_DB"]


class TestConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    MONGO_URI = os.environ["TEST_DB"]


class TestCSRFConfig(TestConfig):
    WTF_CSRF_ENABLED = True


class ProdConfig(Config):
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    MONGO_URI = os.environ["PROD_DB"]
