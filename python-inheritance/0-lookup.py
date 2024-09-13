#!/usr/bin/python3
def lookup(obj):
    my_list = []
    attrs = dir(obj)
    my_list.append(attrs)
    return my_list
