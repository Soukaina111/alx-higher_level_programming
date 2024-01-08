#!/usr/bin/python3
"""Starts a function appending  attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.
    Args:
        obj (any): The object to what to  add an attribute.
        att (str): The attribute name to add to obj.
        value (any): The value of attribute.
    Raises:
        TypeError: If the attribute can't be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
