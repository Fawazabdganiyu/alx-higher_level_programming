#!/usr/bin/python3
if __name__ == "__main__":
    """prints argument lists and their number"""
    from sys import argv
    args = len(argv) - 1
    if args >= 1:
        print("{:d} {:s}:".format(args, "argument"
              if args == 1 else "arguments"))
        index = 1
        while index <= args:
            print("{:d}: {:s}".format(index, argv[index]))
            index += 1
    else:
        print("0 arguments.")
