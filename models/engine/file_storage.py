#!/usr/bin/env python3
"""
A file storing model that saves object instances as a string in a file and converts 
It into Json when used"
"""


from models.base_model import BaseModel
import json

class FileStorage:
    """
    Serializes instances created from the BaseModel class to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json" 
    __objects = {}

    def all(self):
        """
        public instance method that returns the
        dictionary __objects.
        """

    def new(self, obj):
        """
        public instance method that sets in __objects
        the obj with key <obj class name>.id
        Variables:
        ----------
        key [str] -- key format generated.
        """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            Filestorage.__objects[key] = obj

    def save(self):

