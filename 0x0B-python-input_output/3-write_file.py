#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, 'w+', encoding='utf-8') as t_file:
        t_file.write(text)
        return len(text)
