#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    for n in argv[1:]:
        sum += int(n)
    print('{}'. format(sum))
