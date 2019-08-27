#!/usr/bin/python3
"""
script handles error codes
"""
import sys
import urllib.request
import urllib.error
req = urllib.request.Request(sys.argv[1])

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
