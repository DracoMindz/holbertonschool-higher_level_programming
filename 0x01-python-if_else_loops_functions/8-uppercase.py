#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            upp = ord(i) - 32
        else:
            upp = ord(i)
        print("{:c}".format(upp), end="")
    print()
