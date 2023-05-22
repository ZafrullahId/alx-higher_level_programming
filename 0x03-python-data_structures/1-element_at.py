#!/usr/bin/python3
# printing from a list
# Zafrullah Idris

def element_at(my_list, idx):
    """retrieves an element from a list"""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return my_list[idx]
