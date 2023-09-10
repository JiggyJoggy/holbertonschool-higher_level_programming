#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = my_list
        new_list[idx] = element
        return new_list
print(new_in_list([1, 2, 3, 4, 5], 3, 9))
print(new_in_list([1, 2, 3, 4, 5], -10, 7))
