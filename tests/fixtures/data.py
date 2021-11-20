import pytest


@pytest.fixture()
def whitespace_data():
    """
    Create data fixture to test whitespace
    """
    has_whitespace = {"key": "has whitespace"}
    has_leading_whitespace = {"key": " hasleadingwhitespace"}
    has_trailing_whitespace = {"key": "hadtrailingwhitespace "}
    has_no_whitespace = {"key": "nowhitespace"}
    has_empty_value = {"key": ""}
    return [
        has_whitespace,
        has_leading_whitespace,
        has_trailing_whitespace,
        has_no_whitespace,
        has_empty_value,
    ]


@pytest.fixture()
def cursor(mongo):
    """
    Create a cursor fixture to test json parsing
    """
    single = mongo.db.posts.find_one({"username": "test"})
    multiple = mongo.db.posts.find({})
    data = {"single": single, "multiple": multiple}
    return data
