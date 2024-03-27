#!/bin/bash
# This script resent the  request to the same URlthat it come from
 
echo "$(curl -s $1 | wc -c)"
