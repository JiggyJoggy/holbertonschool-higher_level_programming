#!/usr/bin/python3
def no_c(my_string):
    string_list = list(my_string)
    for index in range(len(string_list)):
        if string_list[index] == 'c' or string_list[index] == 'C':
            string_list[index] = None
    new_string = "".join(string_list)
    return new_string
print(no_c("See is not Cee or Cese"))
