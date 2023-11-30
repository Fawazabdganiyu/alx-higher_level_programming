#!/bin/bash
# Display all HTTP methods a server will accept from a URL
curl -sIX OPTIONS "$1" | grep "Allow" | awk -F: '{print $2}' | tr -d '\r ' | sed "s/,/, /g"
