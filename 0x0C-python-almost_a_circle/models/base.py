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


            def load_from_file(cls):
                """load from json"""
                pass

            @classmethod
            def save_to_file_csv(cls, list_objs):
                """serialize file """
                pass

            @classmethod
            def load_from_file_csv(cls):
                """deserialize file"""
                pass

            @staticmethod
            def draw(list_rectangles, list_squares):
                """draw a square"""
