#!/usr/bin/python3
"""

This is a simple module.

"""


def is_kind_of_class(obj, a_class):
    """

    returns True if the object is an instance of, or
    if the object is an instance of a class that inherited
    from, the specified class ; otherwise False.

    Args:
        obj (object): an object.
        a_class (class): a given class.

    Returns:
        bool: true if the object is an instance of or
        an instance of the class that was inherited
        from the specified class, otherwise false.
    """

    return isinstance(obj, a_class)
