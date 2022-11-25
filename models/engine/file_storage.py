#!/usr/bin/env python3
"""
A file storing model that saves object instances as a string in a file and converts 
iIt into Json when used"
"""


from models.base_model import BaseModel
import json

class FileStorage:
    """
    Serializes instances created from the BaseModel class to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "./storage/file.json" 
    __objects = {}

    def all(self):
        """
        public instance method that returns the
        dictionary __objects.
        """
        return FileStorage.__objects

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
            FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the 
        JSON file (path: __file_path)
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, 'w') as my_file:
            json.dump(new_dict, my_file)


