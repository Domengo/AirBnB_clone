#!/usr/bin/env python3
"""
Tests if the FileStorage class can create JSON files when an object instance
is created and load the JSON to the dictionary when needed
"""


from models.engine.file_storage import FileStorage
from unittest import TestCase
from models.base_model import BaseModel


class TestFileStorage(TestCase):
    """
    Testing all edge cases when creating an instance and storing the data
    as JSON file
    """
    
    def setUp(self):
        """
        Used to initialize instances used within the tests
        """
        self.base = BaseModel().to_dict()
        self.base1 = BaseModel(**self.base)
        self.base2 = BaseModel(id="ee49c413-023a-4b49-bd28-f2936c95460d", updated_at="2017-09-28T21:08:06.151750", created_at="2017-09-28T21:08:06.151711")
        self.file_storage = FileStorage()
        self.file_storage.new(self.base1)

    def test_private_attributes(self):
        """
        Tests if the attributes __file_path and __objects are private
        class attributes
        """
        with self.assertRaises(AttributeError):
            self.file_storage.__file_path
            self.file_storage.__objects

