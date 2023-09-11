#!/usr/bin/python3
def no_c(my_string):
    remove_c = {67:None, 99:None}
    new_string = my_string.translate(remove_c)
    return new_string
