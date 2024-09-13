#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        list_copy = self.copy()
        list_copy.sort()
        print (list_copy)
