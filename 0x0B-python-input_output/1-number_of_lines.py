#!/usr/bin/python3
def number_of_lines(filename=""):
    num_lines = 0
    with open(filename, 'r') as f:
        for lines in f:
            num_lines += 1
        return num_lines
