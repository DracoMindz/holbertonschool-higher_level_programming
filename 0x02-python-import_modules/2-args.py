#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    for n, x in enumerate(argv[1:]):
        if len(argv) == 0:
            print(len(argv), 'arguments.')
            exit()
        if len(argv) == 1:
            print(len(argv), 'argument.')
        else:
            print(len(argv), 'arguments:')
        print("{}: {}".format(n, x))
