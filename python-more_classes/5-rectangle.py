#!/usr/bin/python3
"""

This module contains the rectangle class definition.

Classes:
    Rectangle: Represents a simple rectangle shape.

"""


class Rectangle:
    """

    Represents a simple rectangle shape

    """

    def __init__(self, width=0, height=0):
        """

        Initialization of values.

        Args:
            width (int, optional): The width that must
            be greater than or equal to zero. Defaults to 0.
            height (int, optional): The height that must
            be greater than or equal to zero. Defaults to 0.
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """

        Is the getter for the private instance of width.

        Returns:
            int: the width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """

        This sets the private instance of width to the value.

        Args:
            value (int): the value that the width is going to be set too.

        Raises:
            TypeError: width must be an integer.
            ValueError: width must be >= 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """

        This is the getter function for the private instance height.

        Returns:
            int: returns the height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """

        Is the setter for the private instance height.

        Args:
            value (int): value that will be set to height.

        Raises:
            TypeError: height must be an integer.
            ValueError: height must be >= 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """

        Calculates the area of the rectangle.

        Returns:
            int: height times width for area calculation.
        """

        return self.__height * self.__width

    def perimeter(self):
        """_summary_

        Returns:
            int: returns the height multiplied by
            two plus the width multiplied by two.
        """

        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """

        Prints the rectangle on the stdout.

        """

        if self.__height == 0 or self.__width == 0:
            return ""

        result = ""
        for i in range(self.__height):
            for j in range(self.__width):
                result += "#"
            if i != (self.__height - 1):
                result += "\n"

        return result

    def __repr__(self):
        """

        Should return a string representation of the rectangle
        to be able to recreate a new instance.

        Returns:
            str: string representation of the rectangle.
        """

        test = "Rectangle("
        test += str(self.__width)
        test += ", "
        test += str(self.__height)
        test += ")"

        return test

    def __del__(self):
        """

        Simply print the message below when an instance
        is being deleted

        """
        print("Bye rectangle...")
