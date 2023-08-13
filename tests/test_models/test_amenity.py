#!/usr/bin/python3
"""unittests for amenity class"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def setUp(self):
        """Set up method for amenity class
        """
        self.A = Amenity()

    def tearDown(self):
        """Initialized method for class Amenity
        """
        self.A = None

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_unique_id(self):
        """test for unique ids for class objects
        """
        A1 = self.A.__class__()
        A2 = self.A.__class__()
        self.assertNotEqual(self.A.id, A1.id)
        self.assertNotEqual(self.A.id, A2.id)

    def test_id_type_string(self):
        """test id of the class is a string
        """
        self.assertEqual(type(self.A.id), str)

    def test_updated_time(self):
        """test that updated time gets updated
        """
        time1 = self.A.updated_at
        self.A.save()
        sleep(0.5)
        time2 = self.A.updated_at
        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime)

    def test_str_method(self):
        amenity_str = str(self.A)
        self.assertIn("[Amenity]", amenity_str)
        self.assertIn("id", amenity_str)
        self.assertIn("created_at", amenity_str)
        self.assertIn("updated_at", amenity_str)


if __name__ == "__main__":
    unittest.main()
