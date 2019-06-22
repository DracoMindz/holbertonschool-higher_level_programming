#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mia_list = []
    for index in my_list:
        if index == search:
            mia_list.append(replace)
        else:
            mia_list.append(index)
    return (mia_list)
