import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration class."""

    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Strict"


class DevConfig(Config):
    MONGO_URI = os.environ.get("MONGO_DEV_URI")


class TestConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    MONGO_URI = os.environ.get("MONGO_TEST_URI")


class TestCSRFConfig(TestConfig):
    WTF_CSRF_ENABLED = True


class ProdConfig(Config):
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    MONGO_URI = os.environ.get("MONGO_PROD_URI")


config = {
    "dev": DevConfig,
    "test": TestConfig,
    "test_csrf": TestCSRFConfig,
    "prod": ProdConfig,
}
