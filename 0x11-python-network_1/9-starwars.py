#!/usr/bin/python3
""" Python script takes string, sends search request to Star Wars API """
import requests
import sys


if __name__ == '__main__':
    url = 'https://swapi.co/api/people/?search={}'.format(sys.argv[1])
    r = requests.get(url)
    r = dict(r.json())
    print("Number of results: {}".format(len(r.get('results'))))
    for bob in (r.get('results')):
        print(bob.get('name'))
