#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list

    Args:
        my_list: A list that contain any type
        x: The number of elements to be printed from the list

    Return:
        The real number of element printed
    """
    i = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
            i += 1
        except IndexError:
            break
    print()
    return i

if __name__ == "__main__":
    safe_print_list(my_list=[], x=0)
