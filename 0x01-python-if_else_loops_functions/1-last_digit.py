#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_string = "Last digit of {}"
is_string = "is {}"
greater_string = "and is greater than 5"
zero_string = "and is 0"
lessthan_string = "and is less than 6 and not 0"

def lastDigit(number) :
    return (n % 10)

if lastDigit(number) == 0:
print(last_string.format(0)) + (zero_string)
