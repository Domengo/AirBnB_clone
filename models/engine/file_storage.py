#!/usr/bin/env python3
"""
A file storing model that saves object instances as a string in a file and converts 
It into Json when used"
"""


from models.base_model import BaseModel


class FileStorage:
    """
    Serializes instances created from the BaseModel class to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = 
