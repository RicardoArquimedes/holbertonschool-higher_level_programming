#!/usr/bin/python3
"""
Function that print a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """Print the square with the caracter #"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    a = 0
    while a < len(text):
        print("{}".format(text[a]), end="")
        if text[a] in [".", "?", ":"]:
            print("")
            print("")
            a = a + 1
        a = a + 1
