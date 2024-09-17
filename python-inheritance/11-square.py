#!/usr/bin/python3
"""

This is a simple module that describes geometric shapes.

Raises:
    Exception: area() is not implemented.
    TypeError: value is not an integer.
    ValueError: value has to be greater than 0.

Returns:
    bool: None
"""


class BaseGeometry:
    """

    This is a simple class.

    """

    def area(self):
        """

        This method is not implemented.

        Raises:
            Exception: area() is not implemented.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """

        This checks the value inputted and sees if it is
        greater than 0 and an integer.

        Args:
            name (str): variables name.
            value (int): variables value.

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

    This is as simple class that describes a rectangle.

    Args:
        BaseGeometry (cls): the parent class.
    """

    def __init__(self, width, height):
        """

        initializes the dimensions of the rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """

        if super().integer_validator("width", width) is None:
            if super().integer_validator("height", height) is None:
                self.__width = width
                self.__height = height

    def __str__(self):
        """

        prints a formatted string when print() or str() is called.

        Returns:
            str: formatted string
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """

        simple area calculation

        Returns:
            int: the area calculation
        """

        return self.__width * self.__height

class Square(Rectangle):
    """

    A simple class that describes a square.

    Args:
        Rectangle (cls): the parent class.
    """

    def __init__(self, size):
        """

        initializes the values for the width and height for the square.

        Args:
            size (int): the given size.
        """

        super().__init__(size, size)
        self.size = size

    def __str__(self):
        """

        square specific formatted string.

        Returns:
            str: formatted string.
        """

        return "[Square] {}/{}".format(self.size, self.size)
