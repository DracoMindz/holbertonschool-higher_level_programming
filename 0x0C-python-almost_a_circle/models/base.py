#!/usr/bin/python3
import turtle
#base imports turtle
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
                """draw a rectangle in python using turtle"""
                turtle.color(colostring)  # add color to the rectangle
                screen.setup(width = .75, height = .5, startx = None, starty = None)  # screen size, starting point
                startx = self.x
                starty = self.y
                if not isinstance(self.height):
                    self.width = self.height
                for m in range(2):  # draw the rectagle
                    turtle.forward(self.width)
                    turtle.left(90)
                    turtle.forward(self.height)
                    turtle.left(90)
                    
                turtle.exitonclick()  # drawing exits when you click
            #  Task 16
            def save_to_file(cls, list_objs):
                pass
            #  Task 17
            def from_json_string(json_string):
                pass
            #  Task 18
            def create(cls, **dictionary):
                pass
            

