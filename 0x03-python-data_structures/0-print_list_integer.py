#!/usr/bin/python3
# printing from a list
# Zafrullah Idris

def print_list_integer(my_list=[]):
    """print all in the list"""
    for n in range(len(my_list)):
        print("{}".format(my_list[n]))


my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
