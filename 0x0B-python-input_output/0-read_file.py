#!/usr/bin/python3


def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as fi:
        print(fi.read(), end="")
