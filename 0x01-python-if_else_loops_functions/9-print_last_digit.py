#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        lastnumber = (number % -10) * -1
    else:
        lastnumber = (number % 10)
    print('{}'.format(lastnumber), end="")
    return(lastnumber)
