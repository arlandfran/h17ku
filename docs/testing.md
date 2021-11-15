# Testing

To ensure that the development environment is consistent across different machines, the .vscode directory was commited to the repository to ensure that:

1. [Black](https://black.readthedocs.io/en/stable/) is the provided python formatter
2. [Pylint](https://pylint.org/) is the default linter
3. [Pytest](https://docs.pytest.org/en/6.2.x/) is enabled for the test runner

This assumes that you are using Visual Studio Code as your code editor.

## Packages / extensions

- [pytest-flask](https://pytest-flask.readthedocs.io/en/latest/) - Plugin for pytest that provides helpful fixtures and helpers for Flask

- [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) / [coverage.py](https://coverage.readthedocs.io/en/6.1.2/index.html) - Provide code coverage for pytest

- [faker](https://faker.readthedocs.io/en/master/) - Python package that generates fake data

## Setup

Python tests are located in the `/tests` directory and are split into functional tests and unit tests.

The pytest fixtures used for testing are loaded as plugins inside the `conftest.py` file.

The test configuration for Flask enables testing, disables CSRF validation for requests and provides a MONGO_URI that connects to a test database. A CSRF test config is also setup with CSRF validation enabled to test CSRF protection.

## Running the tests

`npm run test` in the terminal to run pytest and generate a code coverage report.

You can also run the tests in VS Code using the built-in test runner. The advantage of this is you can run tests individually, from the side bar or your code, and also debug tests.

## Writing tests

Each test was written following the GIVEN, WHEN, THEN methodology from the BDD (Behaviour Driven Development) paradigm.

```python
"""
GIVEN some sort of state or context
WHEN some action is carried out
THEN describe the results you expect following that action
"""
```

## Fixtures

Fixtures provide their values for test functions to use.

For example:

```python
@pytest.fixture(scope="module")
def mongo():
test_app = create_app(config_name="test")
test_mongo = PyMongo()
  with test_app.test_client():
    with test_app.app_context():
      test_mongo.init_app(test_app)
      yield test_mongo

def test_if_correct_db(mongo): # pass in mongo fixture to test function
    """
    GIVEN a Mongo client
    WHEN connecting to a database during testing
    THEN check the client is connected to the test database
    """
    assert mongo.db.name == "test"
```

This fixture yields a PyMongo client for testing. Setting `scope="module"` means the fixture is destroyed during teardown of the last test in the module.

In this project, any fixture that writes data to MongoDB also cleans itself up on teardown so that the test database doesn't get bloated with any test data.

Fixtures can also request other fixtures. This allows you to compose a generic fixture and then reuse that for different test cases.

For example:

```python
@pytest.fixture(scope="module")
def user(mongo): # uses mongo fixture
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
def different_passwords(user): # uses user fixture
    user = {
        "email": user["email"],
        "username": user["username"],
        "password": "1234",
        "password2": "5678",
    }
    return user
```

> Note that the user fixture _yields_ the user dict instead of returning it. The main reason for this is that any teardown code placed after `yield` is executed automatically by pytest. So say you were to use this fixture to test registration, you may want to remove the registered user from the test database at the end of testing. Since the scope of the fixture is `module`, the code after the yield statement is only executed after every other test in the module is run.
