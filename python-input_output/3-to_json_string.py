#!/usr/bin/python3
"""

This is a simple module.

"""


import json


def to_json_string(my_obj):
    """

    This returns the JSON representation.

    Args:
        my_obj (list): list to be passed through json.

    Returns:
        str: returns str representation.
    """

    return json.dumps(my_obj)
