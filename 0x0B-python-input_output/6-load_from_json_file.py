#!/usr/bin/python3
"""Defining a JSON file-reading function in a module"""
import json

def load_from_json_file(filename):
    """Returns a Python object from a  JSON file that is aready given"""
    with open(filename) as fi:
        return json.load(fi)
