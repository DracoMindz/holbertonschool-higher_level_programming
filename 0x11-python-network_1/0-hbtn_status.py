#!/usr/bin/python3
#write a python script that fetches a url
import urllib

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
