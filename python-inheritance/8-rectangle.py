#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        vtype = type(value)
        if vtype is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        return None

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        if super().integer_validator("width", width) is None:
            if super().integer_validator("height", height) is None:
                self.__width = width
                self.__height = height
