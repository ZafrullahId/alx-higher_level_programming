#!/usr/bin/python3
# 0-lookup.py
# Zafrullah O
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))