#!/usr/bin/python3
"""

This is a simple module.

"""


import json


class Base:
    """

    This is a base class that counts objects.

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """

        This checks if an id is passed in or not.

        Args:
            id (int, optional): An integer that is
            an identifier. Defaults to None.
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json.dumps(list_dictionaries)
