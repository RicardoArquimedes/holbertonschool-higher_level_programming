#!/usr/bin/python3
"""Write a function that returns True
if the object is exactly an instance of
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Function

    Arguments:
    obj --[description]
    a-class -- [description]

    Returns:
    [type] -- [description]
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
