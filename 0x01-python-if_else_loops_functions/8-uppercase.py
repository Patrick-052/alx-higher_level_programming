#!/usr/bin/python3

def uppercase(str):
    upper_cs = ""
    for i in str:
        if 'a' <= i <= 'z':
            upper_cr = chr(ord(i) - 32)
            upper_cs += upper_cr
        else:
            upper_cs += i
    print("{:s}".format(upper_cs))
