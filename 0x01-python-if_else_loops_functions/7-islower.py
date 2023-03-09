#!/usr/bin/python3
alphabets = []
def islower(c):
  for letter in range(97,123):
    alphabets.append(chr(letter))
  if alphabets.__contains__(c):
    return True
  else:
    return False
