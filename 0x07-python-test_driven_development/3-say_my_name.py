#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Function will print first and last name.  Function takes in input.

    Args:
    first_name is input from user or main
    last_name is input from user of main

    Raises:
    TypeError("first_name must be a string")
    TypeError("last_name must be a string")

    Return:
    ("My name is {:s} {:s}".format(first_name, las\|
    t_name))
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
