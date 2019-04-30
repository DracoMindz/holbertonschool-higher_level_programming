#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def lastDigit(num):
    return (number % 10)

if lastDigit(num) == 0:
    print(
        'Last digit of {} is {}'
        'and is zero'
        .format(number, lastDigit(num))

if lastDigit(num) > 5:
    print(
        'Last digit of {} is {} and'
        'is greater than 5'
        .format(number, lastDigit(num))

if lastDigit(num) < 6 and lastDigit(num) != 0:
    print(
        'Last digit of {} is {} and is less'
        'than 6 and not 0'
        .format(number, lastDigit(num))
