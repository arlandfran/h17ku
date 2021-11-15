import re


def find_whitespace(data):
    """
    Loop over data and return True if any value has whitespace
    """
    for value in data.values():
        if re.search(" +", value):
            return True
    return False
