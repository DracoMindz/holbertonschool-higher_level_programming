#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    newlist = my_list.copy()
    return (list(map(lambda x: x * number, my_list)))
