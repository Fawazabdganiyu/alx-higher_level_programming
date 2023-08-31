#!/usr/bin/python3
"""Singly linked list Node definition"""


class Node:
    """defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Instantiate data and next_node

        Args:
            data (int): Data to be stored
            next_node (Node): Pointer to the next node

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: Data to be stored in a node

        Raises:
            TypeError: if `data` is not an integer

        """
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Node: Node object

        raises:
            TypeError: If `next_node` is not None or a Node

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Define a singly linked list"""

    def __init__(self):
        """Instantiate head"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the SinglyLinkedList

        The insertion is in correct sorted position
        in the list (increasing order)

        Args:
            value (int): The new value to be inserted

        """
        new = Node(value)
        if self.__head is None or self.__head.data >= value:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new

    def __str__(self):
        values = []
        current = self.__head
        while current:
            values.append(current.data)
            current = current.next_node
        return '\n'.join(map(str, values))
