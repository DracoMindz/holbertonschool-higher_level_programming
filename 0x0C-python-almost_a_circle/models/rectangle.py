#!/usr/bin/python3

from models.base import Base
"""This module contains the rectangle class"""


class Rectangle(Base):
    """
    Class rectangle that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Private instance attributes, with their own public getter/setter.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        method to get value/properties of private width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setting value for width
        Task 3: TypeError for non integer, ValueError for negative numbers
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if (value < 0):
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        method to get value/properties of private height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setting value of height
        Task 3 TypError for non integer, ValueError for negative numbers
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if (value < 0):
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        method to get values/properties of private
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setting value of x
        Task 3 TypeError for non integer, ValueError for negative numbers
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if (value < 0):
            raise ValueError('x must be >= 0')
            self.__x = value

    @property
    def y(self):
        """
        method to get value/properties of private y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setting value of y
        Task 3 TypeError for non integer. ValueError for negative numbers
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if (value < 0):
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        Task 4 public method area that reurns the area of the Rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Task 5 display the rectangle with "#"
        """
        for x in range(self.height):
            print("#" * self.width)

    def __str__(self, __init__, id=None):
        """
        Task 6: return a string format. call the variables.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def display(self):
        """
        Task 7: Print in stdout instance the Rectagle # character
        """
        print(self.y * '\n', end='')
        for x in range(self.height):
            print(self.x * " " + self.width * "#")

    def update(self, *args, **kwargs):
        """
        Task 8: Assign arguments to each attribute
        """
        k = [id, w, h, x, y]
        for k, v in (key, args):
            if v:
                setattr(self, k. v)

    def to_dictionary(self):
        """
        list of rectangle values
        """
        dictRectangle = {'x': self.x, 'y': self.y, 'id': self.id,
                         'height': self.height, 'width': self.width}
        return dictRectangle
