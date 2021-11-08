import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration class."""

    FLASK_ENV = "development"
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    MONGO_URI = os.getenv("MONGO_DEV_URI")


class TestConfig(Config):
    MONGO_URI = os.getenv("MONGO_TEST_URI")


class ProdConfig(Config):
    FLASK_ENV = "production"
    MONGO_URI = os.getenv("MONGO_PROD_URI")


config = {
    "dev": DevConfig,
    "test": TestConfig,
    "prod": ProdConfig,
}
