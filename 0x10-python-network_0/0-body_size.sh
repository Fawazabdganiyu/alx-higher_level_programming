#!/bin/bash
# Display the size of the body of http response
curl -sI "$1" | grep "Content-Lenght" | awk '{print $2}'
