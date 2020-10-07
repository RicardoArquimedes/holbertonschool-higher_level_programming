#!/usr/bin/python3
"""Read a text file (UTF-8)"""


def read_file(filename=""):
    """Function to read a text file (UTF8)"""
    with open(filename, mode='r') as my_file:
        print(my_file.read())
