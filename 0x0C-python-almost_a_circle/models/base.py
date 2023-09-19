#!/usr/bin/python3
"""
Module Name: models/base.py
Description: This module provides ``Base`` class.
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""
import json


class Base:
    """A simple ``Base`` class definition

    Args:
        id (int): Identification

    Attributes:
        nb_objects (int): A private class attribute

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """A simple class constructor.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): A a list of a dictionary

        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): A list of instances who inherits of Base

        """
        filename = f'{cls.__name__}.json'
        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string

        Args:
            json_string (str): A string representing a list of dictionaries

        Returns:
            list: A list of dictionaries or empty list

        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates instances from a dictionary

        Args:
            **dictionary (kwargs): Variable keyword arguments

        Returns:
            An instance with all attributes already set

        """
        if dictionary is not None and len(dictionary) != 0:
            if cls.__name__ == 'Rectangle':
                dummy = cls(2, 2)
            elif cls.__name__ == 'Square':
                dummy = cls(2)

            dummy.update(**dictionary)

            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances

        Returns:
            A list of dictionary of an instance
            or empty list if file does't exist
        """
        filename = f'{cls.__name__}.json'
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                list_dict = Base.from_json_string(f.read())
                return [cls.create(**inst_dict) for inst_dict in list_dict]
        except FileNotFoundError:
            return []
