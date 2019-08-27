#!/usr/bin/python3
""" Script takes url, send req to url, diplay body response """
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    try:
        req = requests.post(url, data={'q': sys.argv[1]})
    except IndexError:
        req = requests.post(url, data={'q': ""})
    try:
        req = req.json()
        if req:
            print('[{}] {}'.format(req.get('id'), req.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
