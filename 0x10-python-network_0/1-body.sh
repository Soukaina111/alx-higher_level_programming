#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response

url="$1"
outc=$(curl -s -o /dev/null -w "%{http_code}" "$url")

if [ "$outc" -eq 200 ]; then
  curl -s "$url"
else
  echo "Error: Non-200 status code received. Status code: $outc"
fi
