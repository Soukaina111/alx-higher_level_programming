#!/usr/bin/python3
"""Defining a file-appending function for this module."""


def append_write(filename="", text=""):
    """Adds a string to the end of a UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as fi:
        return fi.write(text)
