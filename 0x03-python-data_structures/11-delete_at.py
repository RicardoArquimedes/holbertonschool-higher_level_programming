#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx == -1:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    for list in range(len(my_list)):
        if list == idx:
            del my_list[list]
            return my_list
