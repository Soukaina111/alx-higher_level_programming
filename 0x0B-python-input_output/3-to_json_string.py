#!/usr/bin/python3
"""Defining a string-to-JSON function module"""
import json


def to_json_string(my_obj):
    """Returns the JSON format of a string"""
    return json.dumps(my_obj)
