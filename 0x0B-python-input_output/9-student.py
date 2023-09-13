#!/usr/bi/python3
"""
Module Name: 9-student.py
Description: This module provides ``Student`` class
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


class Student:
    """A definition of Student class

    Attributes:
        first_name (str): The first name of a student
        last_name (str): The last name of a student
        age (int): Age of a student
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
