import pytest
from flask_pymongo import PyMongo

from app import create_app


@pytest.fixture
def app():
    """
    Create application fixture
    pytest-flask will automatically create a test client fixture from this fixture
    """
    test_app = create_app(config_name="test")
    return test_app


@pytest.fixture
def csrf_client():
    """
    Create application fixture with CSRF protection enabled
    """
    csrf_app = create_app(config_name="test_csrf")
    with csrf_app.test_client() as client:
        yield client


@pytest.fixture(scope="module")
def mongo():
    """
    Create Mongo client fixture
    This client connects to the MONGO_URI in the test config
    """
    test_app = create_app(config_name="test")
    test_mongo = PyMongo()
    with test_app.test_client():
        with test_app.app_context():
            test_mongo.init_app(test_app)
            yield test_mongo
