#!/usr/bin/python3
"""
Module 0-add_integer.py
Add two integers
"""


def add_integer(a, b=98):
    """This function add two integers

    Arguments:
        a {int} -- First value of the add

    Keyword Arguments:
        b {int} -- Second value of the add (default: {98})

    Returns:
        [int] -- Result to compute a + b
    """
    e_a = "a must be an integer"
    e_b = "b must be an integer"

    if type(a) != int and type(a) != float:
        raise TypeError(e_a)
    if type(b) != int and type(b) != float:
        raise TypeError(e_b)
    return int(a) + int(b)
