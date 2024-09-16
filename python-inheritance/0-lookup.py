#!/usr/bin/python3
"""

This is a simple module.

"""


def lookup(obj):
    """

    This returns the list of available attributes
    and methods of an object.

    Args:
        obj (list): _description_

    Returns:
        _type_: _description_
    """
    my_list = []
    attrs = dir(obj)
    my_list.append(attrs)
    return my_list
