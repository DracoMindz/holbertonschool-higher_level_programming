#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = []
    if not my_list:
        return None
    for i in my_list:
        if i % 2 == 0:
            newList.append(True)
        if i % 2 != 0:
            newList.append(False)
    return newList
