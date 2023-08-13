#!/usr/bin/python3
"""unittests for amenity class"""

import os
import models
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestUser(unittest.TestCase):
    '''Unit tests for the Amenity class'''

    def tearDown(cls) -> None:
        del cls.amenity

    def setUp(cls):
        cls.amenity = Amenity()
        # self.storage = FileStorage

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_no_args_instantiates(self):
        """checks for no argument"""
        self.assertEqual(Amenity, type(Amenity()))

    def test_amenity_instances(self):
        '''Tests for the obj of the class'''
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_amenity_instances(self):
        '''Tests for the obj of the class'''
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_amenity_str_method(self):
        '''Tests for the str method'''
        expected = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(str(self.amenity), expected)

    def test_amenity_name_type(self):
        ''''tests for the type of name'''
        self.assertEqual(type(self.amenity.name), str)


if __name__ == '__main__':
    unittest.main()
