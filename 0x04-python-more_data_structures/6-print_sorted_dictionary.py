#!/usr/bin/python3
# 6-print_sorted_dictionary.py
# Zafrullah


def print_sorted_dictionary(a_dictionary):
    """Displays a dictionary in the order of keys."""
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]