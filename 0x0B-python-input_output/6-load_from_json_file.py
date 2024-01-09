#!/usr/bin/python3
"""Starts a module defining a JSON file-writing function"""
import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON format"""
    with open(filename, "w") as fi:
        json.dump(my_obj, fi)
