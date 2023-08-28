def safe_print_list(my_list=[], x=0):
    """prints x elements of a list

    Args:
        my_list: A list that contain any type
        x: The number of elements to be printed from the list

    Return: The real number of element printed
    """
    try:
        for i in range(x):
            print(my_list[i], end='')
        print()
        return i + 1
    except IndexError:
        print()
        return i
