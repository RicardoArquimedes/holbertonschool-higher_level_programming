#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for list, element in enumerate(new_list):
        if element is search:
            new_list[list] = replace
    return new_list
