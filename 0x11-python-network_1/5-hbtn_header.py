#!/usr/bin/python3
""" script takes url, send request to url, prints value of var """
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
