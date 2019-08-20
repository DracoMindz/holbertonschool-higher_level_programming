#!/bin/bash
# curl body size
curl -sI $URL | grep -i 'Content-Length'|