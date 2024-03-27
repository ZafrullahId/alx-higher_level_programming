#!/usr/bin/python3
# 4-only_diff_elements.py
# Zafrullah


def only_diff_elements(set_1, set_2):
    """Return a set of all the element present in only one set."""
    return (set_1 ^ set_2)