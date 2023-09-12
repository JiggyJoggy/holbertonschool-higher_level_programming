#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = sum(set(my_list))
    return result
print(uniq_add(my_list=[1, 2, 3, 4, 1, 4,]))
