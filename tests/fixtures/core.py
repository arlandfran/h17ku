import pytest
from flask_pymongo import PyMongo

from app import create_app


@pytest.fixture
def app():
    test_app = create_app(config_name="test")
    return test_app


@pytest.fixture
def csrf_client():
    csrf_app = create_app(config_name="test_csrf")
    with csrf_app.test_client() as client:
        yield client


@pytest.fixture(scope="module")
def mongo():
    test_app = create_app(config_name="test")
    test_mongo = PyMongo()
    with test_app.test_client():
        with test_app.app_context():
            test_mongo.init_app(test_app)
            yield test_mongo
