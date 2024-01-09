#!/usr/bin/python3
"""Ffile-writing function module."""


def write_file(filename="", text=""):
    """displays a string to a UTF8 text file
    """
    with open(filename, "w", encoding="utf-8") as fi:
        return fi.write(text)
