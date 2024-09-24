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

    @property
    def size(self):
        """

        the getter for size

        Returns:
            int: width because it is the same as height.
        """

        return self.__width

    @size.setter
    def size(self, value):
        """

        The setter for size

        Args:
            value (int): the size of the square
        """

        self.width = value
        self.height = value

    @property
    def width(self):
        """

        the overwritten width setter for size

        Returns:
            int: the width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """

        the overwritten setter for width

        Args:
            value (int): the width of the square
        """

        self.__width = self.width_validation(value)

    @property
    def height(self):
        """

        the overwritten height getter

        Returns:
            int: the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """

        the overwritten setter for height

        Args:
            value (int): the height
        """
        self.__height = self.height_validation(value)

    def update(self, *args, **kwargs):
        """

        This method takes non-keyword args and
        updates the instance.

        Args:
            *args (int): variable number of non-keyword args.
            **kwargs (dict): dictionary of keyworded values.
        """

        t = len(args)
        if t > 0:
            self.id = args[0]
            if t > 1:
                self.size = args[1]
                if t > 2:
                    self.x = args[2]
                    if t > 3:
                        self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)