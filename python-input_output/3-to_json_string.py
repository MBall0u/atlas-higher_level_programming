#!/usr/bin/python3
import json
"""

This is a simple module.

"""
def to_json_string(my_obj):
    """

    This returns the JSON representation.

    Args:
        my_obj (list): list to be passed through json.

    Returns:
        str: returns str representation.
    """

    return json.dumps(my_obj)
