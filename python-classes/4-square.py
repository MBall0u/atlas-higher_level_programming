#!/usr/bin/python3
"""

This module contains the square class definition.

Classes:
    Square: Represents a simple square shape.

"""


class Square:
    """

    Represents a simple square shape.

    Attributes:
        size (int): The size of the square.

    """

    def __init__(self, size=0):
        """

        Initializes a square object.

        Args:
            size (int): The size of the square.
        """

        self.__size = size

    @property
    def size(self):
        """

        The getter for the private instance attribute size

        Returns:
            int: the size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """

        Sets the private instance size to value.

        Args:
            value (int): the value of the size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """

        Calculates the area of a square based off the given size.

        Returns:
            Size of the square squared.

        """

        return self.__size ** 2
