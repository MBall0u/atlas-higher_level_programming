#!/usr/bin/python3
"""

This is a simple module.

Raises:
    Exception: area() is not implemented.
    TypeError: value must be an int.
    ValueError: value must be greater than 0.

Returns:
    bool: None
"""


class BaseGeometry:
    """

    This is a simple parent class.

    """

    def area(self):
        """

        This is not implemented.

        Raises:
            Exception: area() is not implemented.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """

        This checks the value and returns None if no
        exceptions are raised.

        Args:
            name (str): variable name.
            value (int): variable value.

        Raises:
            TypeError: value must be an integer.
            ValueError: value must be greater than 0.

        Returns:
            bool: None
        """

        vtype = type(value)
        if vtype is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        return None

class Rectangle(BaseGeometry):
    """

    This is a simple class to describe a rectangle.

    Args:
        BaseGeometry (class): the parent class.
    """

    def __init__(self, width, height):
        """

        This initializes and verifies the inputted values.

        Args:
            width (int): provided width greater than 0.
            height (int): provided height greater than 0.
        """

        if super().integer_validator("width", width) is None:
            if super().integer_validator("height", height) is None:
                self.__width = width
                self.__height = height

    def __str__(self):
        """

        This is a simple print function.

        Returns:
            str: a formatted string.
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """

        This is a simple area calculation.

        Returns:
            int: the width multiplied by the height.
        """

        return self.__width * self.__height
