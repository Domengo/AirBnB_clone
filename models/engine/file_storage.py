#!/usr/bin/env python3
"""
A file storing model that saves
object instances as a string in a file and converts
it into Json when used"
"""


from models.base_model import BaseModel
import json


class FileStorage:
    """
    Serializes instances created from the BaseModel
    class to a JSON file and deserializes
    JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        A method that returns the
        dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        A method that sets in __objects
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
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as my_file:
            json.dump(new_dict, my_file, indent=4)

    def reload(self):
        """
        deserializes __objects if the __file_path exists
        otherwise does nothing
        """
        try:
            with open(
                    FileStorage.__file_path,
                    "r", encoding="utf-8") as json_file:
                for key, obj in json.loads(json_file.read()).items():
                    objects = eval(obj['__class__'])(**obj)
                    FileStorage.__objects[key] = objects
        except FileNotFoundError:
            pass
