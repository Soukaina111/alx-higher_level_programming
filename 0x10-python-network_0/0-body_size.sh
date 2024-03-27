#!/bin/bash
# This script resent the  request to the same URlthat it come from
# While displaying the size of the response's body

outc=$(curl -s $1)
vol=$(echo -n "$outc" | wc -c)

echo "Response body size: $vol bytes"
