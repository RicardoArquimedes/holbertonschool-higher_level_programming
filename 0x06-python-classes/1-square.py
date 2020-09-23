#!/usr/bin/python3

"""1-square.py
The module is a class
The Class defines a square by:
-Private instance attribute: size
-Instantiation with size (no type/value verification)
"""


class Square:
    """
    This is an class Square that defines a square
    Attributes:
        __size (any): The size of square
    """
    def __init__(self, size):
        """
        The constructor for Square class.
        Parameters:
            size (int): The size of square.
        """
        self.__size = size
