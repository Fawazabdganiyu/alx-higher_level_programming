#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operand1 = int(argv[1])
        operator = argv[2]
        operand2 = int(argv[3])
        if operator == "+":
            print("{:d} + {:d} = {:d}".format(operand1, operand2,
                                              add(operand1, operand2)))
        elif operator == "-":
            print("{:d} - {:d} = {:d}".format(operand1, operand2,
                                              sub(operand1, operand2)))
        elif operator == "*":
            print("{:d} * {:d} = {:d}".format(operand1, operand2,
                                              mul(operand1, operand2)))
        elif operator == "/":
            print("{:d} / {:d} = {:d}".format(operand1, operand2,
                                              div(operand1, operand2)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    exit(0)
    """import all functions and
    handle basic operations
    """
