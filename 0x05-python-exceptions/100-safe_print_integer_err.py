#!/usr/bin/python3
def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
        print("Exception: ValueError", file=sys.stderr)
