"""
Module Name: 101-locked_class.py
Description: A `LockedClass` module.
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


class LockedClass:
    """Definition of a `LockedClass` class.

    This class defines no class or object attribute and
    prevents the user from dynamically creating
    new instance attributes, except if the new
    instance attribute is called first_name

    """
    def __setattr__(self, name, value):
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError("'LockedClass' " + "object has no attribute "
                                 + repr(name))
