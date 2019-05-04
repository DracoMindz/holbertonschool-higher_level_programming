#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    ac = len(argv) - 1
    if ac == 0:
        print(ac, 'arguments.')
        exit()
    if ac == 1:
        print(ac, 'argument.')
    else:
        print(ac, 'arguments:')
    for n, x in enumerate(argv[1:], 1):
        print("{}: {}".format(n, x))
