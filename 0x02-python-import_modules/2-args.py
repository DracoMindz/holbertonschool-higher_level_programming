#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 0:
        print(len(argv), 'arguments.')
        exit()
    if len(argv) == 1:
        print(len(argv) - 1, 'argument.')
    else:
        print(len(argv) - 1, 'arguments:')
    for n, x in enumerate(argv[1:]):
        print("{}: {}".format(n, x))
