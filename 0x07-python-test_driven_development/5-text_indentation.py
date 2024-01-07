#!/usr/bin/python3
"""Displays a text with 2 new lines after each,
of : . ? and :
Attributes:
    text_indentation: displays a text with specific conditions
"""


def text_indentation(text):
    """Displays a text with 2 new lines after .?.

    Args:
        text (str): string to be examined.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
