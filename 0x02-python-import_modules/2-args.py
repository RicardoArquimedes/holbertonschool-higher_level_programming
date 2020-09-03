#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

i = 1
if len(argv) == 1:
     print("{:d} arguments.".format(len(argv) - 1))

elif len(argv) == 2:
    print("{:d} arguments:".format(len(argv) - 1))

else:
    print("{:d} arguments:".format(len(argv) - 1))
for a in range(1, len(argv)):
    print("{:d}: {:s}".format(a, argv[a]))
