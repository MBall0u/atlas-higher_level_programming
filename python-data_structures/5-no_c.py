#!/usr/bin/python3
def no_c(my_string):
    for i in (len(my_string)):
        if ord(my_string[i]) != 67 or ord(my_string[i]) != 99:
            print("{}".format(my_string[i]), end='')
