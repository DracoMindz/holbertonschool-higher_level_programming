#!/usr/bin/python3
""" Python script takes string, sends request, manage pagination (json) """
""" StarWars """
import requests
import sys


if __name__ == '__main__':
    url = 'https://swapi.co/api/people/?search={}'.format(sys.argv[1])
    r = requests.get(url)
    print('Number of results: {}'.format(r.json()['count']))
    while r is not None:
        for bob in r.json()['results']:
            print(bob['name'])
        for film in r.json()['films']: 
            print("\t{}".format(bob['title']))
        try:
            r = requests.get(r.json()['next'])
        except:
            break