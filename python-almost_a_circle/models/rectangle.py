#!/usr/bin/python3
"""

This is a simple module.

Returns:
    int: the values being assigned.
"""


from models.base import Base


class Rectangle(Base):
    """

    This is a simple class that describes a rectangle.

    Args:
        Base (cls): the parent class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """

        This is the method that runs when an instance
        initializes.

        Args:
            width (int): the width.
            height (int): the height.
            x (int, optional): optional x. Defaults to 0.
            y (int, optional): optional y. Defaults to 0.
            id (int, optional): optional
            identifier. Defaults to None.
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """

        The getter for the width.

        Returns:
            int: the private attribute width.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """

        The setter for width.

        Args:
            value (int): the value of width.

        Raises:
            TypeError: width must be an integer.
            ValueError: width must be > 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """

        The getter for the height.

        Returns:
            int: the private attribute height.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """

        The setter for height.

        Args:
            value (int): the value of height.

        Raises:
            TypeError: height must be an integer.
            ValueError: height must be > 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """

        The getter for x.

        Returns:
            int: the private attribute x.
        """

        return self.__x

    @x.setter
    def x(self, value):
        """

        The setter for x.

        Args:
            value (int): the value for x.

        Raises:
            TypeError: x must be an integer.
            ValueError: x must be >= 0.
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """

        the getter for y.

        Returns:
            int: the private attribute y.
        """

        return self.__y

    @y.setter
    def y(self, value):
        """

        Th setter for y.

        Args:
            value (int): the value for y.

        Raises:
            TypeError: y must be an integer.
            ValueError: y must be >= 0.
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
