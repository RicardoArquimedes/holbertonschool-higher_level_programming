#!/usr/bin/python3
"""Write a Module that write a file"""


def write_file(filename="", text=""):
    """[summary]

    Keyword Arguments:
        filename {str} -- the file to read(default: {""})
        text {str} -- Text to create in a new file (default: {""})
    """
    with open(filename, mode='w', encoding='utf-8') as my_file:
        return my_file.write(text)
