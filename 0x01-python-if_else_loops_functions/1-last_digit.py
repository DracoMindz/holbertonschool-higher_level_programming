#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last(number):
    return (number % 10)

if last(number) == 0:
    print("Last digit of {} is {}\
          and is zero".format(number, last(number)))

if last(number) > 5:
    print("Last digit of {} is {}\
           and is greater than 5".format(number, last(number)))

if last(number) < 6 and last(number) != 0:
    print("Last digit of {} is {}\
          and is less than 6 and not 0".format(number, last(number)))
