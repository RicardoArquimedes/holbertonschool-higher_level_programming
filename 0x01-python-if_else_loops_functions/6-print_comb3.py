#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if a < b and a != 8:
            print('{:d}{:d}, '.format(a, b), end='')
        if a < b and a == 8:
            print('{:d}{:d}'.format(a, b))
