#!/usr/bin/python3
"""

This is a simple module.

"""
def inherits_from(obj, a_class):
    """

    returns True if the object is an instance of a
    class that inherited (directly or indirectly) from
    the specified class ; otherwise False.

    Args:
        obj (object): object.
        a_class (class): a specified class.

    Returns:
        bool: True if the object is an instance of a
        class that inherited (directly or indirectly)
        from the specified class ; otherwise False.
    """

    obj_type = type(obj)
    if obj_type == a_class:
        return False
    elif issubclass(obj_type, a_class):
        return True
    else:
        return False
