#!/usr/bin/python3
"""

This is a simple module.

"""


import json


def save_to_json_file(my_obj, filename):
    """

    This writes a json string to a file.

    Args:
        my_obj (obj): an object
        filename (str): file name
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
