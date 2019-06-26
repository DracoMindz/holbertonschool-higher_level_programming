#!/usr/bin/python3
def safe_print_integer_err(value):

    try:
        valueConvertedToAnInt = int(value)
        print(valueConvertedToAnInt)
        return True
    except Exception as error:
        print("Exception:", error)
        return False
