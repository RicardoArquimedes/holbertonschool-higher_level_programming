#!/usr/bin/python3

"""3-square.py
This module contains an class
A class that defines a square by:
-Private instance attribute: size
-Instantiation with size(optional): def __init__(self, size=0)
"""


class Square:
    """
    This is an class Square that defines a square
    Attributes:
        __size (int): The size of square
        size must be an integer that is 0 or greater
    """
    def __init__(self, size=0):
        """
        The constructor for Square class.
        Parameters:
            size (int): The size of square.
        """
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size

    def area(self):
        """
        This function calculates the area of a square
         Returns:
            Square: The area of a square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        This property is to get it back
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This property is to configure it
        """
        self.__size = value

    def my_print(self):
        """
        this function prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
