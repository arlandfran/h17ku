import pytest

from app.helpers import find_whitespace, parse_json


def test_find_whitespace_helper(whitespace_data):
    """
    GIVEN the find_whitespace helper and whitespace data
    WHEN the helper is called with different data values
    THEN check that the function evaluates each value correctly
    """
    results = []
    for data in whitespace_data:
        results.append(find_whitespace(data))

    assert results[0] is True  # has whitespace
    assert results[1] is True  # has leading whitespace
    assert results[2] is True  # has trailing whitespace
    assert results[3] is False  # has no whitespace
    assert results[4] is False  # has empty value

    with pytest.raises(AttributeError) as error:
        find_whitespace({"key"})  # no value

    assert error.type is AttributeError
    assert error.value.args[0] == "'set' object has no attribute 'values'"


def test_parse_json_helper(cursor):
    """
    GIVEN the parse_json helper and cursor data
    THEN when the helper is called with different cursor data
    THEN check that helper parses the data correctly
    """
    single = parse_json(cursor.get("single"))
    multiple = parse_json(cursor.get("multiple"))
    assert isinstance(single, dict)
    assert isinstance(multiple, list)
    for document in multiple:
        assert isinstance(document, dict)
