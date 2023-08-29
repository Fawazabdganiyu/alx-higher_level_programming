#!/usr/bin/python3
def safe_print_division(a, b):
    """divides 2 integers and prints the result.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result


if __name__ == "__main__":
    safe_print_division(2, 1)
