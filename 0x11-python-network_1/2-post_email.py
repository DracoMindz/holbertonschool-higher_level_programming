#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data_e = data.encode('ascii')
    request = urllib.request.Request(url, data_e)
    with urllib.request.urlopen(request) as response:
        print(response.decode())
