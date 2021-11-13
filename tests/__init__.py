from faker import Faker
from faker.providers import internet, misc

fake = Faker()
fake.add_provider(internet)
fake.add_provider(misc)


valid = {
    "email": fake.ascii_safe_email(),
    "username": fake.user_name(),
    "password": fake.password(length=8),
}

invalid_email = {
    "email": valid["email"],
    "username": fake.user_name(),
    "password": fake.password(length=8),
}

invalid_username = {
    "email": fake.ascii_safe_email(),
    "username": valid["username"],
    "password": fake.password(length=4),
}

invalid_password = {
    "email": fake.ascii_safe_email(),
    "username": fake.user_name(),
    "password": fake.password(length=4),
}

test_user = {
    "valid": valid,
    "invalid_email": invalid_email,
    "invalid_username": invalid_username,
    "invalid_password": invalid_password,
}
