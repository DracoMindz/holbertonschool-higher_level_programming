#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r') as f:
        alllinesinf = f.readlines()
        if nb_lines <= 0 or nb_lines > len(alllinesinf):
            for eachline in alllinesinf:
                print(eachline.rstrip('\n'))
        else:
            for index in range(nb_lines):
                print(alllinesinf[index].rstrip('\n'))
