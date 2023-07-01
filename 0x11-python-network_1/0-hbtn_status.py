#!/usr/bin/python3
"""Fetching content from a URL using urllib"""
import urllib.request as ur


if __name__ == "__main__":
    with ur.urlopen('https://alx-intranet.hbtn.io/status') as res:
        cont = res.read()

    print("Body response:")
    print("    - type: {}".format(type(cont)))
    print("    - content: {}".format(cont))
    print("    - utf8 content: {}".format(cont.decode('utf-8')))
