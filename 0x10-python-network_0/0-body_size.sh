#!/bin/bash
# This script resent the  request to the same URlthat it come from
# While displaying the size of the response's body
 
size=$(curl -s $1 | wc -c)

echo "Response body size: $size bytes"
