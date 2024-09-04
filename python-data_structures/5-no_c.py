#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for i in (my_string):
        if ord(i) == 67 or ord(i) == 99:
            print("", end='')
        else:
            new_string += i
    return new_string
