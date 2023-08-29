#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers.

    Args:
        my_list: A list with any type
        x: The number of elements to access in my_list

    Return:
        The real number of integers printed
    """
    ret = 0
    i = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
        except (TypeError, ValueError):
            ret += 1
            continue
    print()
    return i - ret


if __name__ == "__main__":
    safe_print_list_integers(my_list=[1, 2, 3, 4, 5], x=2)
