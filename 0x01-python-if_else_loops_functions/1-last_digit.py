#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    m = number % 10
else:
    m = number % -10

print("Last digit 0f {} is " .format(number), end="")

if m < 6 and m != 0:
    print("{} and is less than 6 and not 0".format(m))
if m > 5:
    print("{} and is greater than 5".format(m))
if m == 0:
    print("{} and is 0".format(m))
