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
    if not a:
        raise TypeError("a must be an integer")
    if not b:
        raise TypeError("b must be an integer")
    if a and b:
        continue
    if not isinstance(a, (int, float)):
        raise ValueError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise ValueError('b must be an integer')
    sum = int(a) + int(b)
    return(sum)
