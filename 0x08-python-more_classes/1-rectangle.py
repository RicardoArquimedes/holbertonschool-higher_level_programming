#!/bin/usr/python3

"""0-square.py
This module write a class Rectangle that defines a
rectanble by:(based on 0-rectangle.py)
"""


class Rectangle:
    """class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """construtor
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def height(self):
        """Getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter
        """

        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

        @property
        def width(self):
            """getter
            """

        @width.setter
        def width(self, value):
            """setter
            """
            if type(value) != int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value