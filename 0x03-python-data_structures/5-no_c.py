#!/usr/bin/python3
# printing from a list
# Zafrullah Idris

def no_c(my_string):
  """remove C or c from the string"""
  new_string = []
  for l in my_string:
    if not (l == "C" or l == "c"):
      new_string.append(l)
  return "".join(new_string)
