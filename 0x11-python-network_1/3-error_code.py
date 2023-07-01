#!/usr/bin/python3
"""Sending a request to a url specified and
   displaying he body as well as handling a HTTPError"""
import urllib.request as ur
import urllib.error as uer
from sys import argv


if __name__ == "__main__":
    try:
        with ur.urlopen(argv[1]) as res:
            cont = res.read().decode('utf-8')
    except uer.HTTPError as e:
        print("Error code: ", e.code)
    else:
        print(cont)
