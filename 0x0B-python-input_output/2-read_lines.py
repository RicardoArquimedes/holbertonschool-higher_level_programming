#!/usr/bin/python3
"""Write a  module it create a function that read
    n lines of a file
"""


def read_lines(filename="", nb_lines=0):
    """This  function that reads n lines of a text file
    (UTF8) and prints it to stdout:
    Arguments:
        filename {str} -- This is the file to read(default: {""})
        nb_lines {int} -- This is the number line to read(default: {0})
    """
    lines = 0
    with open(filename, 'r', encoding='utf-8') as my_file:
        while True:
            rd = my_file.readline()
            if rd is '':
                break
            print("{}".format(rd), end="")
            lines += 1
            if lines == nb_lines:
                break
