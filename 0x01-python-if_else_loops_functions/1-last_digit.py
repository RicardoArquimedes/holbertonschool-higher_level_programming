#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
m = n % 10

if m > 5:
    print("Last digit of {:d} is, and is greater than 5" .format(n, m))
elif m == 0:
    print("Last digit of {:d} is, and is 0" .format(n, m))
else:
    print("Last digit of {:d} is, and is less than 6 and not 0" .format(n, m))
