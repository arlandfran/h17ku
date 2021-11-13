import pytest
from flask_pymongo import PyMongo
from flask_login import LoginManager

from app import create_app
from app.models import User


@pytest.fixture
def app():
    test_app = create_app(config_name="test")
    return test_app


@pytest.fixture(scope="module")
def mongo():
    test_app = create_app(config_name="test")
    test_mongo = PyMongo()
    with test_app.test_client():
        with test_app.app_context():
            test_mongo.init_app(test_app)
            yield test_mongo


@pytest.fixture(scope="module")
def new_user():
    user = User("test@test.com", "test_user")
    return user
