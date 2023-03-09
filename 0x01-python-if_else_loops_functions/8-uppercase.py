#!/usr/bin/python3
def uppercase(str):
    word = ""
    for l in str:
        if int(ord(l)) >= 97 and int(ord(l)) < 123:
            word += chr(int(ord(l)) - 32)
        else:
            word += l
    return word
