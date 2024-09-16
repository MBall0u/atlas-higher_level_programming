#!/usr/bin/python3
"""

This is a simple module.

"""


class MyList(list):
    """

    This prints the inputted list, but sorted.

    Args:
        list (list of ints): unsorted list.
    """
    def print_sorted(self):
        list_copy = self.copy()
        list_copy.sort()
        print (list_copy)
