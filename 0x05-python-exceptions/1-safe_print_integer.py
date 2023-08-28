#!/usr/bin/python3
def safe_print_integer(value):
    """prints an integer with "{:d}".format()

    Args:
        value: expected integer to be printed

    Return:
        True if value has been correctly printed
        (it means the value is an integer)
        Otherwise, returns False
    """
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return False
    else:
        return True


if __name__ == "__main__":
    safe_print_integer(25)
