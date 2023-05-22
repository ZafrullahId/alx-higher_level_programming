#!/usr/bin/python3
# printing from a list
# Zafrullah Idris

def max_integer(my_list=[]):
    """find the biggest integer of a list."""
    max = 0
    if len(my_list) == 0:
        return None
    for n in my_list:
        if n > max:
            max = n
    return max
