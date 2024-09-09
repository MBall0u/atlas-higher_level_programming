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

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        
        Calculates the area of a square based off the given size.
        
        Returns:
            Size of the square squared.
        
        """
        
        return self.__size ** 2

    pass
