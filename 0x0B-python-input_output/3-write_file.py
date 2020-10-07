#!/usr/bin/python3
"""Write a Module that write
in a new file"""


def write_file(filename="", text=""):
    """Keyword Arguments:
        filename {str} -- the file to read(default: {""})
        text {str} -- Text to create in a new file (default: {""})
    """   
    with open(filename, mode='w', encoding='utf-8') as my_file:
        return my_file.write(text)
