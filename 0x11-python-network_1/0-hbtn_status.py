#!/usr/bin/python3
"""Fetching content from a URL using urllib"""
import urllib.request as ur


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with ur.urlopen(url) as res:
        cont = res.read()

    print("Body response:")
    print(f"\t- type: {type(cont)}")
    print(f"\t- content: {cont}")
    print(f"\t- utf8 content: {cont.decode('utf-8')}")
