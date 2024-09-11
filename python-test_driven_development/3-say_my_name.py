#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """

    Prints a simple message stating the name.

    Args:
        first_name (str): The first name provided.
        last_name (str, optional): The last name provided.
        Defaults to "".

    Raises:
        TypeError: first_name must be a string.
        TypeError: last_name must be a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
