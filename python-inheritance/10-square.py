#!/usr/bin/python3
"""

Raises:
    Exception: _description_
    TypeError: _description_
    ValueError: _description_

Returns:
    _type_: _description_
"""


class BaseGeometry:
    """



    """

    def area(self):
        """



        Raises:
            Exception: _description_
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """



        Args:
            name (_type_): _description_
            value (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_

        Returns:
            _type_: _description_
        """

        vtype = type(value)
        if vtype is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        return None

class Rectangle(BaseGeometry):
    """



    Args:
        BaseGeometry (_type_): _description_
    """

    def __init__(self, width, height):
        """



        Args:
            width (_type_): _description_
            height (_type_): _description_
        """

        if super().integer_validator("width", width) is None:
            if super().integer_validator("height", height) is None:
                self.__width = width
                self.__height = height

    def __str__(self):
        """



        Returns:
            _type_: _description_
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """



        Returns:
            _type_: _description_
        """

        return self.__width * self.__height

class Square(Rectangle):
    """



    Args:
        Rectangle (_type_): _description_
    """

    def __init__(self, size):
        """



        Args:
            size (_type_): _description_
        """

        super().__init__(size, size)
