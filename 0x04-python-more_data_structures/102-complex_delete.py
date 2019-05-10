#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    allPairs = a_dictionary.items()
    byeKeys = []

    for eachallPairs in allPairs:
        if eachallPairs[1] == value:
            byeKeys.append(eachallPairs[0])

    for key in byeKeys:
        del a_dictionary[key]
    return (a_dictionary)
