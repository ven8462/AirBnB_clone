#!/usr/bin/python3
"""test user"""

from unittest.mock import patch
import unittest
from models.user import User
from models.engine.file_storage import FileStorage
import os


class TestUser(unittest.TestCase):
    '''Test cases for the `User` class.'''

    def setUp(self):
        """Set up method for User class
        """
        self.Us = User()

    def tearDown(self):
        """Initialized User class
        """
        self.Us = None

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(User.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(User.__doc__) >= 1)

    def test_basic_attribute_set(self):
        """Basic attribute tests for user model
        """
        self.Us.first_name = 'Lavender'
        self.Us.last_name = 'Gituku'
        self.assertEqual(self.Us.first_name, 'Lavender')
        self.assertEqual(self.Us.last_name, 'Gituku')


if __name__ == '__main__':
    unittest.main()
