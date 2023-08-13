#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
import os
import models
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlaceInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def setUp(self):
        """set up method for place class
        """
        self.P = Place()

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_type(self):
        """test method for type testing of place
        """
        self.assertIsInstance(self.P, Place)
        self.assertEqual(type(self.P), Place)
        self.assertEqual(issubclass(self.P.__class__, Place), True)
        self.assertEqual(isinstance(self.P, Place), True)

    def test_string_return(self):
        """tests the string method
        """
        string = str(self.P)
        Pid = "[{}] ({})".format(self.P.__class__.__name__,
                                 self.P.id)
        test = Pid in string
        self.assertEqual(True, test)
        test = "updated_at" in string
        self.assertEqual(True, test)
        test = "created_at" in string
        self.assertEqual(True, test)
        test = "datetime.datetime" in string
        self.assertEqual(True, test)

    def test_unique_id(self):
        """test for unique ids for class objects
        """
        P1 = self.P.__class__()
        P2 = self.P.__class__()
        self.assertNotEqual(self.P.id, P1.id)
        self.assertNotEqual(self.P.id, P2.id)

    def test__str__(self):
        """tests the string representation"""
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.__str__(), pl2.__str__())

    def test_updated_time(self):
        """test that updated time gets updated
        """
        time1 = self.P.updated_at
        self.P.save()
        time2 = self.P.updated_at
        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime)

    def test_to_dict_type(self):
        """verifys the class returns a dictionary"""
        pl = Place()
        self.assertTrue(dict, type(pl.to_dict()))


if __name__ == '__main__':
    unittest.main()
