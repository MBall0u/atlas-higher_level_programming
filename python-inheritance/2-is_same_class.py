#!/usr/bin/python3
def is_same_class(obj, a_class):
    obj_type = type(obj)
    if obj_type == a_class:
        return True
    else:
        return False
