#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if search == 0:
        return my_list.copy()
    if search > len(my_list) - 1:
        return my_list.copy()
    for new in range(len(my_list)):
        if search - 1 == new:
            new_list = my_list.copy()
            new_list[new] = replace
            return new_list
