def uppercase(str):
    for l in str:
        if int(ord(l)) >= 97 and int(ord(l)) < 123:
            l = chr(int(ord(l)) - 32)
        print("{}".format(l),end="")
    print()
