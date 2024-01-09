#!/usr/bin/python3
"""Starts a JSON-to-object function Module"""


import json

def from_json_string(my_str):
    """Shows the Python object format of a JSON string object"""
    return json.loads(my_str)
