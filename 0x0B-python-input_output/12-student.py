#!/usr/bin/python3

"""
Student class
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        newDict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                newDict[key] = value
        return (newDict)
