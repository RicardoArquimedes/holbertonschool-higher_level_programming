#!/usr/bin/python3

"""4-rectangle.py
This module write a class Rectangle 
by: (based on 3-rectangle.py)
"""

class Rectangle: 
    """class Rectangle that defines a rectangle
    """
    __error_1 = "width must be an integer"
    __error_2 = "height must be >= 0"

    def __init__(self, width=0, height=0):
        """constructor
        """
        if type(width) != int:
            raise TypeError(Rectangle.__error_1)
        elif width < 0:
            raise ValueError(Rectangle.__error_2)
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError(Rectangle.__error_1)
        elif width < 0:
            raise ValueError(Rectangle.__error_2)
        else:
            self.__height = height