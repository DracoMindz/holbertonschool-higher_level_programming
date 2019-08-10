#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)
    
    if operator not in ["+", "-", "/", "*"]:
        print("Unknown operator. Available operators: +, -, * and /\n")
        exit(1)
    elif operator is "+":
        result = a + b
        print("{:d} + {:d} = {:d}".format(a, b, result))
    elif operator is "-":
        result = a - b
        print("{:d} - {:d} = {:d}".format(a, b, result))
    elif operator is "*":
        result = a * b
        print("{:d} * {:d} = {:d}".format(a, b, result))
    elif operator is "/":
        result = a / b
        print("{:d} / {:d} = {:d}".format(a, b, result))    
