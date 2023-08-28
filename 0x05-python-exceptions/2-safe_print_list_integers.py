#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers.

    Args:
        my_list: A list with any type
        x: The number of elements to access in my_list

    Return:
        The real number of integers printed
    """
    i = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
        except (TypeError, ValueError):
            i -= 1
            continue
    print()
    return i


if __name__ == "__main__":
    safe_print_list_integers(my_list=[], x=0)
