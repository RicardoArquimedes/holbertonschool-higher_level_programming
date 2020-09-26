#!/usr/bin/python3
"""
Function that print a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Arguments:
    text: letter in text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    tmp = 0
    for i, c in enumerate(text):
        if c in ".?:":
            print(text[tmp:i + 1].strip(), end="\n\n")
            tmp = i + 1
        elif i == len(text) - 1:
            print(text[tmp:i + 1].strip(), end="")
