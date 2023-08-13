#!/usr/bin/python3

import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            self.storage.all(None)

    def test_all(self):
        self.assertEqual(dict, type(FileStorage().all()))

    def test_new_adds_object(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save_writes_correct_data(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        with open(self.storage._FileStorage__file_path, "r") as f:
            data = f.read()
            self.assertIn(f"{obj.__class__.__name__}.{obj.id}", data)

    def test_reload_creates_objects(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()

        loaded_objects = self.storage.all()
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", loaded_objects)

    def test_reload_method(self):
        model = BaseModel()
        model_id = model.id
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        objects = self.storage.all()
        key = f"BaseModel.{model_id}"
        self.assertIn(key, objects)
        self.assertTrue(isinstance(objects[key], BaseModel))

    def test_new_method(self):
        model = BaseModel()
        model_id = model.id
        self.storage.new(model)
        objects = self.storage.all()
        self.assertIn(f"BaseModel.{model_id}", objects)


if __name__ == '__main__':
    unittest.main()
