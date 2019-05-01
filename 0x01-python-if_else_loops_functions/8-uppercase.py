#!/usr/bin/python3
def uppercase(str):
    for i in range(65, 91):
        var = ord(i)
        print("{:c}".format(var + 32), end="")
