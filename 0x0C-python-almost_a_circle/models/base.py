#!/usr/bin/python3
class Base:
    """
    This class will be the base of all other classes
    """
    __nb_objects = 0

    def __init__(self, id=None): #instantiates class
        if id is not None: #public attribute or property
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
