#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

print('Last digit of {}'.format(number), end=" ")

if (number < 0):
    lastnumber = ((-1 * number) % 10) * -1
elif (number > 0):
    lastnumber = (number % 10)
else:
    lastnumber = 0

if (lastnumber) == 0:
    print('is {} and is zero'.format(lastnumber))

if (lastnumber) > 5:
    print('is {} and is greater than 5'.format(lastnumber))

if (lastnumber) < 6 and (number % 10) != 0:
    print('is {} and is less than 6 and not 0'.format(lastnumber))
