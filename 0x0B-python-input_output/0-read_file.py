#!/usr/bin/python3
"""defining a text file-reading function"""


def read_file(filename=""):
    """shows the content of a UTF8 text file"""
    with open(filename, encoding="utf-8") as fi:
        print(fi.read(), end="")
