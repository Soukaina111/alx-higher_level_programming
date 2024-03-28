#!/usr/bin/python3
""" This script Write a Python script
    that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    Link = "https://alx-intranet.hbtn.io/status"
    req = requests.get(Link)
    print("Body response:")
    print("\t- type:", type(req.text))
    print("\t- content:", req.text)
