#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

b = len(argv) - 1
if b == 0:
    print('arguments.')

else:
    print(len(argv) - 1, 'arguments:')
    for a in range(1, len(argv)):
        print("{}: {}".format(a, argv[a]))
