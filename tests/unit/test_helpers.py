import pytest

from app.helpers import find_whitespace


def test_find_whitespace_helper():
    """
    WHEN the helper is called with different data values
    THEN check that the function evaluates each value correctly
    """
    assert find_whitespace({"email": "has whitespace"}) is True
    assert find_whitespace({"email": "hasnowhitespce"}) is False
    assert find_whitespace({}) is False
    with pytest.raises(AttributeError) as error_info:
        find_whitespace({"email"})
    assert error_info.type is AttributeError
    assert error_info.value.args[0] == "'set' object has no attribute 'values'"
