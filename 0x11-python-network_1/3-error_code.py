#!/usr/bin/python3
""" script handles error codes, take in url"""
import sys
import urllib.request


if __name__ == "__main__":
    bob = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(bob) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
