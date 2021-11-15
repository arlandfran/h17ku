import pytest


@pytest.fixture()
def whitespace_data():
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
