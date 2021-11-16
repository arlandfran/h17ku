import re
import json
from bson import json_util


def find_whitespace(data):
    """
    Loop over data and return True if any value has whitespace
    """
    for value in data.values():
        if re.search(" +", value):
            return True
    return False


def parse_json(data):
    """Parses input data and returns JSON"""
    return json.loads(json_util.dumps(data))
