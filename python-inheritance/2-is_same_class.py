#!/usr/bin/python3
"""

This is a simple module.

"""


def is_same_class(obj, a_class):
    """

    Returns true if the given object is exactly an
    instance of the specified class.

    Args:
        obj (object): any object.
        a_class (class): a specified class.

    Returns:
        bool : true if exact instance of specified class
        otherwise false.
    """
    obj_type = type(obj)
    if obj_type == a_class:
        return True
    else:
        return False
