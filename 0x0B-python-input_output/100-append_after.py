#!/usr/bin/python3
"""defines a text file insertion function module"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file
    """
    text = ""
    with open(filename) as re:
        for line in re:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as wr:
        wr.write(text)
