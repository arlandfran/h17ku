import pytest
from faker import Faker
from faker.providers import internet, misc
from werkzeug.security import generate_password_hash

fake = Faker()
fake.add_provider(internet)
fake.add_provider(misc)


@pytest.fixture(scope="module")
def fake_user(mongo):
    """
    Create fake user fixture
    Fake user is inserted into test database and then deleted on teardown
    """
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
    """
    Create fake user fixture for registration
    Fake user is deleted from test database on teardown
    """
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
def email_exists(fake_user):
    """
    Create fake user fixture for registration that uses an existing email in test database
    """
    same_password = fake.password(length=8)
    user = {
        "email": fake_user["email"],
        "username": fake.user_name(),
        "password": same_password,
        "password2": same_password,
    }
    return user


@pytest.fixture()
def username_exists(fake_user):
    """
    Create fake user fixture for registration that uses an existing username in test database
    """
    user = {
        "email": fake.ascii_safe_email(),
        "username": fake_user["username"],
        "password": fake_user["password"],
        "password2": fake_user["password"],
    }
    return user


@pytest.fixture()
def different_passwords():
    """
    Create fake user fixture for registration that has non matching passwords
    """
    user = {
        "email": fake.ascii_safe_email(),
        "username": fake.user_name(),
        "password": fake.password(length=8),
        "password2": fake.password(length=8),
    }
    return user
