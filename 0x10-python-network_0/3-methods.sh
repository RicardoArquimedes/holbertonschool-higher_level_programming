#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods
curl -s -I "$1" | grep "Allow" | cut -d " " -f2-
