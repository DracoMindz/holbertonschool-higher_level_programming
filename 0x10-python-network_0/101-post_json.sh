#!/bin/bash
#Script sends a JSON POST, request URL as argument,
curl -X POST -H "Content-Type: application/json" -d "@$2" "$1"
