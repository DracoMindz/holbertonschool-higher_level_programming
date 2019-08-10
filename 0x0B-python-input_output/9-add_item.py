#!/usr/bin/python3
import json
import sys
import os.path


saveFile = __import__('7-save_to_json_file').save_to_json_file
loadFile = __import__('8-load_from_json_file').load_from_json_file


mylist = []

if os.path.exists('add_item.json'):
    mylist = loadFile('add_item.json')

for b in sys.argv[1:]:
    mylist.append(b)

saveFile(mylist, "add_item.json")
