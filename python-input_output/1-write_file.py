#!/usr/bin/python3
"""

This is a simple module.

"""


def write_file(filename="", text=""):
    """

    This writes to a file.

    Args:
        filename (str, optional): the filename that is
        being wrote. Defaults to "".
        text (str, optional): The input that is being
        wrote to the file. Defaults to "".

    Returns:
        int: number of characters.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        characters = f.write(text)
    return characters
