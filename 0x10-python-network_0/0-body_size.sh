#!/bin/bash
# Takes in URL, send URL, display size of body in response
curl  -sI $URL |wc -c