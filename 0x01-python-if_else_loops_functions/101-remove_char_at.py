#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        i = str[:n]
        j = str[n + 1:]
        return i + j
    if n < 0:
        i = str[:n]
        j = str[n:]
        return i + j
