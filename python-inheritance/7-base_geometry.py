#!/usr/bin/python3
"""



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
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
