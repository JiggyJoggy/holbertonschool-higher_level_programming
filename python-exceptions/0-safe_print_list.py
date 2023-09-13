#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element = 0
    for index in rage(x):
        try:
            print(my_list[index], end="")
            element += 1
        except IndexError:
            break
    print()
    return element
