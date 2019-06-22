#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    c = 0
    try:
        for i in my_list:
            if i <= x:
                print("{}".format(my_list[i-1]), end="")
                i += 1
                c += 1
    except IndexError:
        print()
    print("")
    return(c)
