#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 122:
            new_string += chr(ord(str[i]) - 32)
        else:
            new_string += str[i]
    print("{}".format(new_string))
