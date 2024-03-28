#!/usr/bin/python3

""" This script fetches a url and read the responses component """
from urllib.request import Request, urlopen

if __name__ == "__main__":

	req = Request('https://alx-intranet.hbtn.io/status')
	with urlopen(req) as res:
		 html = res.read()
		 print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
                         .format(type(html), html, html.decode("utf-8")))
