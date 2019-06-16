#!/usr/bin/bash
from models.base import Base
from models.rectangle import Rectangle
"""
Class Square: inherits from rectangle. Height and width equal size
"""


class Square(Rectangle):


    def __init__(self, size, x=0 , y=0, id=None):
    """
    Instance attributes, with getter and setter. Task 10        
    """
        Rectangle.__init__(width, height, x, y, id)
	
	width = height
	size = width
	self.x = x
	self.y = y
	self.size = size

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
	
     """
     Task 12: create a public method assigning attributes
     """
     def update(self, *args, **kwargs):
         args = [id, size, x, y]
	 for k, v in (kwargs, args):
            if v:
                setattr(self, k. v)


