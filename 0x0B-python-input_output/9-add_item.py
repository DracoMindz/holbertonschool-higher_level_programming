#!/usr/bin/python3
import json
import sys


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as filename:
        json.dump(my_obj, filename)


def load_from_json_file(filename):
    """
    function to load json object
    """
    with open(filename) as f:
        return json.load(f)


def add_item(args):
    """
    function to add all arguemts to a Python List and save to json file
    """

    myList = []
    myListList = mylist.extend(args)
    save_to_json_file(myListList, add_item.js)
    load_from_json_file(add_item.js)
