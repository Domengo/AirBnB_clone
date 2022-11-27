#!/usr/bin/env python3
"""Tests for the Base model class"""


from models.base_model import BaseModel
from unittest import TestCase


class TestBaseModel(TestCase):
    """Tests all the edge cases in the base model class"""

    def setUp(self):
        """Reduces redundancy in each test case"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def test_str(self):
        """
        Testing if the attributes
        required to be a string are actually a string
        """
        self.assertIsInstance(self.base1.id, str)
        self.assertIsInstance(self.base2.id, str)

    def test_instance(self):
        """
        Testing if the created instances
        are instances of the BaseModel class
        """
        self.assertIsInstance(self.base1, BaseModel)
        self.assertIsInstance(self.base2, BaseModel)

    def test_save_method(self):
        """
        Tests all the functionalities of the save function
        """
        self.assertNotEqual(self.base1.updated_at, self.base2.updated_at)


if __name__ == "__main__":
    unittest.main()
