#!/usr/bin/python3
""" Python script takes 2 argv, sends search request to GitHUb """
import requests
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    r = requests.get(url, auth=(username, password))
    r = dict(r.json())
    print(r.get('id'))
