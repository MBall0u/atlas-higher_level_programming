#!/usr/bin/python3
"""

This prints the inputted list, but sorted

"""


class MyList(list):
    def print_sorted(self):
        list_copy = self.copy()
        list_copy.sort()
        print (list_copy)
