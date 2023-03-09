#!/usr/bin/python3
for n in range(0, 100):
    for x in range(0,10):
        if not n >= x:
            if str(n) + str(x) == "89":
                print("{}{}".format(n,x))
            else:
                print("{}{}".format(n,x),end=", ")
