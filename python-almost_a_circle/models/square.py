#!/usr/bin/python3

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width
        )
