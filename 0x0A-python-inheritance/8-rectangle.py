#!/usr/bin/python3
class BaseGeometry:

    def area(self):

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("<name> must be an integer").format())
        if value <= 0:
            raise ValueError("<name> must be greater than 0").format())


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator("width", width, int)
        self.__width = width
        super().integer_validator("height", height, int)
        self.__height = height
