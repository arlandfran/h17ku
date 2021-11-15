import pytest
from faker import Faker
from faker.providers import internet, misc
from werkzeug.security import generate_password_hash

from app.models import User, load_user

fake = Faker()
fake.add_provider(internet)
fake.add_provider(misc)


@pytest.fixture()
def new_user():
    user = User("test@test.com", "test_user")
    return user


@pytest.fixture()
def user_loader():
    return load_user


@pytest.fixture()
def user_class():
    return User


@pytest.fixture()
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
    yield user
    mongo.db.users.delete_one({"email": user["email"]})


@pytest.fixture(scope="module")
def new_fake_user(mongo):
    same_password = fake.password(length=8)
    user = {
        "email": fake.ascii_safe_email(),
        "username": fake.user_name(),
        "password": same_password,
        "password2": same_password,
    }
    yield user
    mongo.db.users.delete_one({"email": user["email"]})


@pytest.fixture()
def email_exists(new_fake_user):
    user = {
        "email": new_fake_user["email"],
        "username": fake.user_name(),
        "password": new_fake_user["password"],
        "password2": new_fake_user["password"],
    }
    return user


@pytest.fixture()
def username_exists(new_fake_user):
    user = {
        "email": fake.ascii_safe_email(),
        "username": new_fake_user["username"],
        "password": new_fake_user["password"],
        "password2": new_fake_user["password"],
    }
    return user


@pytest.fixture()
def different_passwords(new_fake_user):
    user = {
        "email": new_fake_user["email"],
        "username": new_fake_user["username"],
        "password": fake.password(length=8),
        "password2": fake.password(length=8),
    }
    return user
