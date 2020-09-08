#!/usr/bin/python3
def no_c(my_string):
    no_c_string = ''
    for c in my_string:
        if c not in 'Cc':
            no_c_string += c
    return(no_c_string)
