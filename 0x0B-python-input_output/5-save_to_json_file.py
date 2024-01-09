#!/usr/bin/python3
"""Starts a JSON file-writing function module"""
import json

def save_to_json_file(my_obj, filename):
    """Writes an object in a text file using JSON representation"""
    with open(filename, "w") as fi:
        json.dump(my_obj, fi)
