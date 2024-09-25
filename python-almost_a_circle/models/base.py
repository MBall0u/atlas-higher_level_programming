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
        """

        converts a dictionary to a json string

        Args:
            list_dictionaries (dict): a dictionary

        Returns:
            str: either empty of json str
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """

        writes the JSON string representation of
        list_objs to a file.

        Args:
            list_objs (list): list of instances of base
        """

        new_list = cls.to_json_string(list_objs)

        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(new_list, f)
