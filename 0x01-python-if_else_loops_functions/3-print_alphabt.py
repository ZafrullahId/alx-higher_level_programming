#!/usr/bin/python3
for letter in range(97, 123):
  if chr(letter) != 'q' or chr(letter) != 'e':
    print(f"{chr(letter)}",end=" ")
