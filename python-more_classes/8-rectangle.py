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

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol

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
                result += str(self.print_symbol)
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
        is being deleted.

        """

        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """

        checks the area of one instance of Rectangle vs another.

        Args:
            rect_1 (class): first instance.
            rect_2 (class): second instance.

        Raises:
            TypeError: rect_1 must be an instance of Rectangle.
            TypeError: rect_2 must be an instance of Rectangle.

        Returns:
            class: The rectangle with the largest area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        results1 = rect_1.area
        results2 = rect_2.area

        if results1 >= results2:
            return rect_1
        else:
            return rect_2