#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response
vol=$(curl -sI $1 | awk '/Content-Length/ {print $2}')
echo "Response body size: $size bytes"
