#!/usr/bin/python3
# printing from a list
# Zafrullah Idris

def print_reversed_list_integer(my_list=[]):
    """print in reverse order"""
    new_list = []
    for i in  range(len(my_list) - 1,-1,-1):
        new_list.append(my_list[i])

    return new_list
