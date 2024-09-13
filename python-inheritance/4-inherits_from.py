#!/usr/bin/python3
def inherits_from(obj, a_class):
    obj_type = type(obj)
    if obj_type == a_class:
        return False
    elif issubclass(obj_type, a_class):
        return True
    else:
        return False
