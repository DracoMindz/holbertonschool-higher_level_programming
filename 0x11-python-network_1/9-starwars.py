#!/usr/bin/python3
""" Script takes url, send req to url, diplay body response """
import requests
import sys


if __name__ == '__main__':
    url = 'https://swapi.co/api/people/?search={}'.format(sys.argv[1])
    r = requests.get(url)
    r = dict(r.json())
    print("Number of results: {}".format(len(r.get('results'))))
    for bob in (r.get('results')):
        print(bob.get('name'))
