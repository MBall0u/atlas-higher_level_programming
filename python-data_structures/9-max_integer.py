#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        max = my_list[0]
        for i in my_list[1:]:
            if max < i:
                max = i
        return max
