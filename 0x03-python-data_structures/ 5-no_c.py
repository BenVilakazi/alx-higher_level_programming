#!/usr/bin/python3
def no_c(my_string):
    new_list = ""
    j = 0
    for i in my_string:
        if (i not in 'cC'):
            new_list += my_string[j]
        j += 1
    return (new_list)