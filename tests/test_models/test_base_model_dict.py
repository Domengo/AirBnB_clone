#!/usr/bin/env python3

"""
Unittests of the implemented
BaseModel extention to accept dictionaries as input
"""


import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModelCreationFromDict(unittest.TestCase):
    """
    Contains all the TestCases for the unittests
    """

    def setUp(self):
        """
        Avoids repetition of creating
        duplicate instances in each test case
        """
        self.base = BaseModel().to_dict()
        self.basedict = BaseModel(**self.base)
        self.base1 = BaseModel(
                created_at="2017-09-28T21:03:54.052298",
                updated_at="2017-09-28T21:03:54.052302")

    def test_conversion_to_datetime_obj(self):
        """
        checks if the created BaseModel object from dictionary
        contains a created_at attribute of type datetime.datetime
        """
        self.assertEqual(type(self.base1.created_at), datetime.datetime)
        self.assertEqual(type(self.base1.updated_at), datetime.datetime)

    def test_if_class_is_an_instance_attribute(self):
        """
        checks if __class__ is an instance attribute when
        an instance is created from a dictionary when
        passed in as kwargs. If it exists there is an error
        """
        self.assertNotIn("__class__", self.basedict.__dict__)
