#!/usr/bin/python3
if __name__ == "__main__":
    """prints the result of the addition of all arguments"""
    from sys import argv
    args = len(argv) - 1
    if args == 0:
        print("0")
    else:
        result = 0
        index = 1
        while index <= args:
            result += int(argv[index])
            index += 1
        print(result)
