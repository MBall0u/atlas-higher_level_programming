#!/usr/bin/python3
"""

This is a simple module.

"""


def append_write(filename="", text=""):
    """

    appends text to a file.

    Args:
        filename (str, optional): the given file that the text
        is being appended to. Defaults to "".
        text (str, optional): the text that is being append to
        the file. Defaults to "".

    Returns:
        int: the number of characters written.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        characters = f.write(text)
    return characters
