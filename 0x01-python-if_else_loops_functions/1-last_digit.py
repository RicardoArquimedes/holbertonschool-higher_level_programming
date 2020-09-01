#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
m = number % 10
str = 'last digit of'

if m > 5:
    print("{} {} is {} and is greater than 5" .format(str, number, m))
elif m == 0:
    print("{} {} is {} and is 0" .format(str, number, m))
else:
    print("{} {} is {} and is less than 6 and not 0" .format(str, number, m))
