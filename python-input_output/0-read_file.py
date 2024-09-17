#!/usr/bin/python3
"""

This is a simple module.

"""


def read_file(filename=""):
    """

    This reads a file and prints it.

    Args:
        filename (str, optional): File to read from.
        Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
