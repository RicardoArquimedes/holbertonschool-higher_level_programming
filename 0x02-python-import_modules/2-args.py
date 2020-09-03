#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

if len(argv) == 0:
    print(len(argv) - 1, 'arguments.')

elif len(argv) == 1:
    print("{:d} arguments:".format(len(argv) - 1))

else:
    print("{:d} arguments:".format(len(argv) - 1))
    for a in range(1, len(argv)):
        print("{:d}: {:s}".format(a, argv[a]))
