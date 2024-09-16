#!/usr/bin/python3
"""

This returns the list of available attributes
and methods of an object.

"""


def lookup(obj):
    my_list = []
    attrs = dir(obj)
    my_list.append(attrs)
    return my_list
