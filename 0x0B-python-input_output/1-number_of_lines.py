#!/usr/bin/python3
"""Return numbers of lines"""


def number_of_lines(filename=""):
        """Function that read a file and count number of lines.
        Args:
            filename (str, optional): file path. Defaults to "".
        """
        with open(filename, mode='r', encoding="utf-8") as my_file:
            for i, l in enumerate(my_file):
                pass
        return i
