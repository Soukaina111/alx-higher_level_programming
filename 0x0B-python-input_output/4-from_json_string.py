#!/usr/bin/python3
"""Starts a module defines a JSON-to-object function"""


import json


def from_json_string(my_str):
    """Returns the Python object format  of a JSON string"""
    return json.loads(my_str)
