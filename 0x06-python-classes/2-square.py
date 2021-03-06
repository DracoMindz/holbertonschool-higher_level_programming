#!/usr/bin/python3
class Square:
    """A shape with 4 equal sides and 4 right angles."""
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
