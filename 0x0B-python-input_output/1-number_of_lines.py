#!/usr/bin/python3
"""Return numbers of lines"""


def number_of_lines(filename=""):
        """Function that read a file and count number of lines.
        Args:
            filename (str, optional): file path. Defaults to "".
        """
        i = 0
        with open(filename, mode='r', encoding="utf-8") as my_file:
            for line in my_file:
                i = i + 1
            return i
