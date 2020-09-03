#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

b = len(argv) - 1
if b == 0:
    print(len(argv) - 1, 'arguments.')

elif b == 1:
    print(len(argv) - 1, 'arguments:')
    print("{:d}: {:s}".format(b, argv[b]))

else:
    print(len(argv) - 1, 'arguments:')
    for a in range(1, len(argv)):
        print("{:d}: {:s}".format(a, argv[a]))
