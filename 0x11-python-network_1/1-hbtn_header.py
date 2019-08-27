#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
Displays the value of the X-Request-Id variable
from the header of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    arg_url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(arg_url) as response:
        print(response.info().get('X-Request-Id'))
