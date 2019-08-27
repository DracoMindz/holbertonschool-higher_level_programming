#!/usr/bin/python3
"""
script handles error codes
"""
import urllib.request
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError

req = Request(sys.argv[1])

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: ', e.code)
