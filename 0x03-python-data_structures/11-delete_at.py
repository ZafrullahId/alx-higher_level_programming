#!/usr/bin/python3
# printing from a list
# Zafrullah Idris

def delete_at(my_list=[], idx=0):
    if idx < 0 and idx > len(my_list) - 1:
        return my_list
    my_list.remove(my_list[idx])
    return my_list
