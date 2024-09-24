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
        self.__width = self.width_validation(width)
        self.__height = self.height_validation(height)
        self.__x = self.x_validation(x)
        self.__y = self.y_validation(y)

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
        """

        self.__width = self.width_validation(value)

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
        """

        self.__height = self.height_validation(value)

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
        """

        self.__x = self.x_validation(value)

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
        """

        self.__y = self.y_validation(value)

    @classmethod
    def width_validation(cls, value):
        """

        The width validation method.

        Args:
            value (int): the value of width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0

        Returns:
            int: the value
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        return value

    @classmethod
    def height_validation(cls, value):
        """

        the height validation method

        Args:
            value (int): the value of height

        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0

        Returns:
            int: the value
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        return value

    @classmethod
    def x_validation(cls, value):
        """

        The x validation method

        Args:
            value (int): the value of x

        Raises:
            TypeError: x must be an integer
            ValueError: x must be >= 0

        Returns:
            int: the value
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        return value

    @classmethod
    def y_validation(cls, value):
        """

        The validation method for y

        Args:
            value (int): the value of y

        Raises:
            TypeError: y must be an integer
            ValueError: y must be >= 0

        Returns:
            int: the value
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        return value

    def area(self):
        """

        The method that returns the area

        Returns:
            int: the area of the rectangle
        """

        return self.__width * self.__height

    def display(self):
        """

        This method prints out the inputted rectangle
        dimensions.

        """

        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            print("")

    def __str__(self):
        """

        This prints formatted information for rectangle.

        Returns:
            str: formatted string
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(seld.id, self.__x, self.__y, self.__width, self.__height)
