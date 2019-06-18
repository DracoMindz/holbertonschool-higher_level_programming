#!/usr/bin/python3
if__name__ == "__main__":
    from sys import argv
    from calculator_1.py import add, sub, mul, div

    if len(argv) not 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)

     operator = argv[2]
     a = int(argv[1])
     b = int(argv[3])

     if operator not "+" or "-" or "/" or "*":
         print("Unknown operator. Available operators: +, -, * and /\n")
         exit(1)
     if operatotor is "+":
         a + b = result
         print("{:d} + {:d} = {:d}".format(a, operator, b, result)
     if operator is "-":
         a - b = result
         print("{:d} - {:d} = {:d}".format(a, operator, b, result)
     if operator is "*":
         a * b = result
         print("{:d} * {:d} = {:d}".format(a, operator, b, result)
     if operator is "/":
         a / b = result
         print("{:d} / {:d} = {:d}".format(a, operator, b, result)    
