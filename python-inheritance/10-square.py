#!/usr/bin/python3
"""

This is a simple module.

Raises:
    Exception: area() not implemented.
    TypeError: value must be an integer.
    ValueError: value must be greater than 0.

Returns:
    bool: None
"""


class BaseGeometry:
    """

    This is a simple class describing a base geometry shape.

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

        Checks the value and make sure of two things:
        That it is an integer and that it is greater than 0.

        Args:
            name (str): variables name.
            value (int): variables value.

        Raises:
            TypeError: value is not an integer.
            ValueError: value is not greater than 0.

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

    This is a simple class that describes a rectangle.

    Args:
        BaseGeometry (cls): the parent class.
    """

    def __init__(self, width, height):
        """

        intializes the rectangles width and height.

        Args:
            width (int): provided width.
            height (int): provided height.
        """

        if super().integer_validator("width", width) is None:
            if super().integer_validator("height", height) is None:
                self.__width = width
                self.__height = height

    def __str__(self):
        """

        prints a formatted string if str() or print() is called.

        Returns:
            str: a formatted string.
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """

        Does a simple calculation for the area of the rectangle.

        Returns:
            int: the area.
        """

        return self.__width * self.__height

class Square(Rectangle):
    """

    This is a simple class that describes a square.

    Args:
        Rectangle (cls): the parent class.
    """

    def __init__(self, size):
        """

        initializes the size of the square into the parent
        classes width and height variables.

        Args:
            size (int): the width and height of the square.
        """

        super().__init__(size, size)
