#!/usr/bin/python3
"""Fetching content from a URL using urllib"""
import urllib.request as ur


if __name__ == "__main__":
    with ur.urlopen('https://alx-intranet.hbtn.io/status') as res:
        cont = res.read()

    print("Body response:")
    print(f"    - type: {type(cont)}")
    print(f"    - content: {cont}")
    print(f"    - utf8 content: {cont.decode('utf-8')}")
