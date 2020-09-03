#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

b = 1
if len(argv) == 0:
    print(len(argv) - 1, 'arguments.')

elif len(argv) == 1:
    print("{:d} arguments.".format(len(argv) - 1))

else:
    print(len(argv) - 1, 'arguments:')
    for a in range(1, len(argv)):
        print("{:d}: {:s}".format(a, argv[a]))
