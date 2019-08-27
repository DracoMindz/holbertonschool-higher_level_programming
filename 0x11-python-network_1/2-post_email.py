#!/usr/bin/python3
"""
takes two areguements, first is url second is email
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    dat = urllib.parse.urlencode(values)
    dat = dat.encode('ascii')
    request = urllib.request.Request(url, dat)
    with urllib.request.urlopen(request) as response:
        print(response.decode().decode('utf-8'))
