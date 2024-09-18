#!/usr/bin/python3
"""

converts json string to obj.

Returns:
    list: json string converted.
"""


import json


def from_json_string(my_str):
    """

    returns an object represented by a json string.

    Args:
        my_str (str): inputted string.

    Returns:
        obj: object
    """

    return json.load(my_str)
