#!/usr/bin/bash
from models.base import Base
from models.rectangle import Rectangle
"""
Class Square: inherits from rectangle. Height and width equal size.
"""


class Square(Rectangle):

    squarescalled = 0

    def __init__(self, size, x=0 , y=0, id=None):
"""
Instance attributes, with getter and setter. Task 10.
"""
        Rectangle.__init__(width, height, x, y, id)
        width = height
        size = width
        self.size
        self.x = x
        self.y = y

    sqaurescalled += 1

    @property   # method to get value/properties of width
    def width(self):
        Rectangle.width(self)

    @width.setter # setting the width, for square is the same as height
    def width(self, value):
        Rectangle.width(self, value)  #  inherit from Rectangle
    
    @property # method in heritted from Rectangle
    def height(self):
        Rectangle.height(self)

    @height.setter  # setting the value of the height
    def height(self, value):
        Rectangle.height(self, value)

    @property  # method to get values/property of x
    def x(self):
        Rectangle.x(self)

    @x.setter
    def x(self, value):  # setting value of x
        Rectangle.x(self, value)

    @property  # method to get value of y
    def y(self):
        Rectangle.y(self)

    @y.setter
    def y(self, value): # setting value of y
        Rectangle.y(self, value)

    #  call the method __str__
    obj.__str__(self, __init__, id=None):
        return "[{}] ({}) {}/{} - {}".format("Square", self.id, self.x, self.y, self.width)

        """
        Task 11: create a public getters and setters for size
        """
     @property   # method to get value of private size                    
    def size(self):
        return self.__size

    @size.setter  # setting value of size                                          
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be > 0')
        self.__size = value




