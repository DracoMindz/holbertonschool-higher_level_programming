#!/usr/bin/python3
from models.base import Base
"""
Class rectangle that inherits from Base.
"""


class Rectangle(Base):

    rectanglesCalled = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Private instance attributes, with their own public getter/setter.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    rectanglesCalled += 1

    @property   # method to get value/properties of private width
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
        Task 3: TypeError for non integer, ValueError for negative
numbers
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if (value < 0):
            raise ValueError('width must be > 0')
        self.__width = value

    @property  # method to get value/properties of private height
    def height(self):
        return self.__height

    @height.setter   # setting value of height
    def height(self, value):

        """
        Task 3 TypError for non integer, ValueError for negative nu
mbers
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if (value < 0):
            raise ValueError('height must be > 0')
        self.__height = value

    @property   # method to get values/properties of private x
    def x(self):
        return self.__x

    @x.setter   # setting value of x
    def x(self, value):
        """
        Task 3 TypeError for non integer, ValueError for negative n
umbers
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if (value < 0):
            raise ValueError('x must be >= 0')
            self.__x = value

    @property   # methos to get value/properties of private y
    def y(self):
        return self.__y

    @y.setter   # setting value of y
    def y(self, value):

        """
        Task 3 TypeError for non integer. ValueError for negative numbers
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if (value < 0):
            raise ValueError('y must be >= 0')
        self.__y = value

        """
        Task 4 public method area that reurns the area of the Rectangle
        """
    def area(self):
        return self.width * self.height

        """
        Task 5 display the rectangle with "#"
        """
    def display(self):
        for x in range(self.height):
            print("#" * self.width)

        """
        Task 6: return a string format. call the variables.
        """

    def __str__(self, __init__, id=None):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
        """
        Task 7: Print in stdout instance the Rectagle # character
        """
    def display(self):
        print(self.y * '\n', end='')
        for x in range(self.height):
            print(self.x * " " + self.width * "#")
        """
        Task 8: Assign arguments to each attribute
        """
    def update(self, *args, **kwargs):
        k = [id, w, h, x, y]
        for k, v in (key, args):
            if v:
                setattr(self, k. v)

    def to_dictionary(self):
        dictRectangle = {'x': self.x, 'y': self.y, 'id': self.id,
                         'height': self.height, 'width': self.width}
        return dictRectangle
