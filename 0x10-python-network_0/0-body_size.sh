#!/bin/bash
# Displays the size of the body of the HTTP response header for a given URL
curl -s "$1" | wc -c
