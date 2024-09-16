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

    my_list = []
    attrs = dir(obj)
    my_list.append(attrs)
    return my_list
