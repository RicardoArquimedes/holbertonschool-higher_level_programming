#!/usr/bin/python3

"""3-rectangle.py
This module write a class Rectangle
by: (based on 2-rectangle.py)
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

    @property
    def height(self):
        """getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter
        """
        if type(value) != int:
            raise TypeError(Rectangle.__error_1)
        elif value < 0:
            raise ValueError(Rectangle.__error_2)
        else:
            self.__height = value

    @property
    def width(self):
        """getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter
        """
        if type(value) != int:
            raise TypeError(Rectangle.__error_1)
        elif value < 0:
            raise ValueError(Rectangle.__error_2)
        else:
            self.__width = value

    def area(self):
        """This function renturn the area
        """
        return self.__width * self.__height

    def perimeter(self):
        """This function return the perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """print the rectangle with the character >#
        """
        rectangle_1 = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle_1
        for x in range(self.__height - 1):
            rectangle_1 += ("#" * self.__width) + "\n"
        rectangle_1 += ("#" * self.__width)
        return rectangle_1
