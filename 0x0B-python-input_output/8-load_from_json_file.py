#!/usr/bin/python3
"""
json object pass
"""
import json


def load_from_json_file(filename):
    """
    function to load json object
    """
    with open(filename) as f:
        return json.load(f)
