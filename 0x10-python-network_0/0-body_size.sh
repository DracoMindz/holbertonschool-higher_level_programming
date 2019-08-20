#!/bin/bash
# Takes in URL, send URL, display size of body in response
curl -Is "$1" |wc -c