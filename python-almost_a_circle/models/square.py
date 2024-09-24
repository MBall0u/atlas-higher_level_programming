#!/usr/bin/python3
"""

This is a simple module describing a square.

Returns:
    str: a formatted string
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """

    This is a child class of rectangle.

    Args:
        Rectangle (cls): the parent class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """

        This method initializes the attributes.

        Args:
            size (int): the height and width of the square.
            x (int, optional): the height offset. Defaults to 0.
            y (int, optional): the width offset. Defaults to 0.
            id (int, optional): an identifier. Defaults to None.
        """

        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """

        returns a formatted string

        Returns:
            str: a formatted string
        """

        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width
        )
