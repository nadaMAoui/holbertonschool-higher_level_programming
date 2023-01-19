#!/usr/bin/python3
def uppercase(str):
    key = 0
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            key = 32
        else:
            key = 0
        print("{:c}".format(ord(i) - key), end="")
    print()
