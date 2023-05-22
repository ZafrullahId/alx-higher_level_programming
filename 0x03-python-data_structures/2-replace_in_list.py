#!/usr/bin/python3
# printing from a list
# Zafrullah Idris

def replace_in_list(my_list, idx, element):
    """replaces an element of a list at a specific"""
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    my_list[idx] = element
    return my_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
print(replace_in_list(my_list, idx, new_element))
