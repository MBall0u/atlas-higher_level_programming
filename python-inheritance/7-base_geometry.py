#!/usr/bin/python3
"""

This is a simple module.

"""


class BaseGeometry:
    """

    This is a simple base class.

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

        This is going to check the value and make sure it
        is an integer and greater than 0.

        Args:
            name (str): given name.
            value (int): given integer.

        Raises:
            TypeError: must be an integer.
            ValueError: must be greater than 0.
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
