#!/usr/bin/python3
import urllib.request
import sys
if __name__ == "__main__":
    sys.argv[1] = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info().get('X-Request-Id'))
