#!/bin/bash
# Display on an HTTP response status coode
curl -sI "$1" | grep -e "HTTP.*" | awk '{print $2}' | tr -d '\r\n'
