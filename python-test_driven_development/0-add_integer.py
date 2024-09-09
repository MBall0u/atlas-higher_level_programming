#!/usr/bin/python3
"""

This is a simple module where we are just adding a two integers together.

"""


def add_integer(a, b=98):
    """

    Adds two integers together.

    Args:
        a (int or float): The first number to add. Must be provided.
        b (int or float): The second number to add. Optional, defaults to 98.

    Raises:
        TypeError: If either a or b is not an integer or float.

    Returns:
        int: The sum of a and b as integers.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
