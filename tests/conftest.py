import pytest
from flask_pymongo import PyMongo
from faker import Faker
from faker.providers import internet, misc
from werkzeug.security import generate_password_hash


from app import create_app
from app.models import User, load_user


fake = Faker()
fake.add_provider(internet)
fake.add_provider(misc)


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


@pytest.fixture(scope="module")
def user_loader():
    yield load_user


@pytest.fixture(scope="class")
def user_class():
    yield User


@pytest.fixture(scope="module")
def fake_user(mongo):
    password = fake.password(length=8)
    pwd_hash = generate_password_hash(password)
    user = {
        "email": fake.ascii_safe_email(),
        "username": fake.user_name(),
        "password": password,
        "pwd_hash": pwd_hash,
    }
    mongo.db.users.insert_one(
        {
            "email": user["email"],
            "username": user["username"],
            "pwd_hash": user["pwd_hash"],
        }
    )
    return user


@pytest.fixture(scope="module")
def new_fake_user():
    same_password = fake.password(length=8)
    user = {
        "email": fake.ascii_safe_email(),
        "username": fake.user_name(),
        "password": same_password,
        "password2": same_password,
    }
    return user


@pytest.fixture(scope="function")
def email_exists(new_fake_user):
    user = {
        "email": new_fake_user["email"],
        "username": fake.user_name(),
        "password": new_fake_user["password"],
        "password2": new_fake_user["password"],
    }
    return user


@pytest.fixture(scope="function")
def username_exists(new_fake_user):
    user = {
        "email": fake.ascii_safe_email(),
        "username": new_fake_user["username"],
        "password": new_fake_user["password"],
        "password2": new_fake_user["password"],
    }
    return user


@pytest.fixture(scope="function")
def different_passwords(new_fake_user):
    user = {
        "email": new_fake_user["email"],
        "username": new_fake_user["username"],
        "password": fake.password(length=8),
        "password2": fake.password(length=8),
    }
    return user
