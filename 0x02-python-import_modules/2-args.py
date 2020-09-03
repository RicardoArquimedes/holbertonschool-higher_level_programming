#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) < 2:
        print("{}".format(len(argv) - 1), "arguments.")
    elif len(argv) == 2:
        print("{}".format(len(argv) - 1), "arguments:")
    else:
        print("{} {}".format(len(argv) - 1, "arguments:"))
    for a in range(1, len(argv)):
        print("{}: {}".format(a, argv[a]))
