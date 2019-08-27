#!/usr/bin/python3
""" Script takes url, send req to url, diplay body response """
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code == r.raise_for_status:
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
