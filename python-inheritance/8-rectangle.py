#!/usr/bin/python3
"""

This is a simple module.

Raises:
    Exception: area() is not implemented.
    TypeError: must be an integer.
    ValueError: must be greater than 0.

Returns:
    bool: None
"""


class BaseGeometry:
    """

    This is a simple base class.

    """

    def area(self):
        """

        This is not implemented for the base class.

        Raises:
            Exception: area() is not implemented.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """

        This type checks and sees if the value is greater than 0.

        Args:
            name (str): name of the variable.
            value (int): value of the given variable.

        Raises:
            TypeError: must be an integer.
            ValueError: must be greater than 0.

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

    This is a derived class from BaseGeometry.

    Args:
        BaseGeometry (class): parent class.
    """

    def __init__(self, width, height):
        """

        This initializes the width an height in the parent class.

        Args:
            width (int): provided width.
            height (int): provided height.
        """

        if super().integer_validator("width", width) is None:
            if super().integer_validator("height", height) is None:
                self.__width = width
                self.__height = height
