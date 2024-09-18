#!/usr/bin/python3
"""

This is a simple module.

Returns:
    obj: json object
"""


import json


def load_from_json_file(filename):
    """

    creates an Object from a “JSON file”.

    Args:
        filename (str): file name

    Returns:
        obj: obj created from json file.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
