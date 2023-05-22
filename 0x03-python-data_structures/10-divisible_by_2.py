#!/usr/bin/python3
# printing from a list
# Zafrullah Idris

def divisible_by_2(my_list=[]):
    """find all multiples of 2 in a list."""
        new_list = []
        for n in my_list:
            if n % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
                
        return new_list
