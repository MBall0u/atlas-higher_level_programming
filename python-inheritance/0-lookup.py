#!/usr/bin/python3
"""

This is a simple module.

"""


def lookup(obj):
    """

    This returns the list of available attributes
    and methods of an object.

    Args:
        obj (list): object.

    Returns:
        list: returns the list of available attributes
        and methods.
    """

    my_list = dir(obj)
    return my_list
