#!/usr/bin/python3
import sys
argv = sys.argv

b = len(argv) - 1
if b == 0:
    print('arguments.')

else:
    print(len(sys.argv) - 1, 'arguments:')
    for a in range(1, len(argv)):
        print("{}: {}".format(a, argv[a]))
