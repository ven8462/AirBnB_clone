#!/usr/bin/python3
"""test base_model"""

import unittest
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def setUp(self):
        """Set up method for object BM of BAseModel"""
        self.BM = BaseModel()

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_no_args_instantiates(self):
        """test is basemodel is an instance of Basemodel"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        """test if id is a string"""
        self.assertEqual(str, type(BaseModel().id))

    def test_unique_id(self):
        """test for id in BaseModel objects
        """
        BM1 = BaseModel()
        BM2 = BaseModel()
        self.assertNotEqual(self.BM.id, BM1.id)
        self.assertNotEqual(self.BM.id, BM2.id)

    def test_save_method(self):
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        new_updated_at = my_model.updated_at
        self.assertNotEqual(original_updated_at, new_updated_at)

    def test_basic_attribute_set(self):
        """test method for basic attribute assignment
        """
        self.BM.first_name = 'Lavender'
        self.BM.last_name = 'Gituku'
        self.assertEqual(self.BM.first_name, 'Lavender')
        self.assertEqual(self.BM.last_name, 'Gituku')


if __name__ == "__main__":
    unittest.main()
