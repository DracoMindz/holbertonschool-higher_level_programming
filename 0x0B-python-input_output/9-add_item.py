#!/usr/bin/python3
import json
import sys
import os.path


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file



myList = []

if os.path.exists("add_item.json"):
    myList = load_from_json_file('add_item.json')

for b in sys.argv[1:]:
    myList.append(b)

save_to_json_file(myList, "add_item.json")
