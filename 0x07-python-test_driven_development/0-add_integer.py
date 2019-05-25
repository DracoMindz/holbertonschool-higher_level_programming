#!/usr/bin/python3
def add_integer(a, b=98):
"""
Function adds integers

Args:
a and b are integers

Raises:
TypeError("a must be an integer")
TypeError("b must be an integer")

Return: Sum
"""

    sum  = int(a) + int(b)

    if not isinstance(a, int) or  not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return(sum)
