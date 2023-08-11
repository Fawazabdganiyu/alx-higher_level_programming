#!/usr/bin/python3
if __name__ == "__main__":
    """imports  function add from a file and prints
    the result of the addition 1 + 2 = 3
    """
    from add_0 import add
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
