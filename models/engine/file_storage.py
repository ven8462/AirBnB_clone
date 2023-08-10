#!/usr/bin/python3
"""
FileStorage module
"""
from models.base_model import BaseModel
import json
import os


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        """
        new_dict = {}

        for key in self.__objects.keys():
            new_dict[key] = self.__objects[key].to_dict()

        with open(self.__file_path, "w") as fobj:
            json.dump(new_dict, fobj)
        """

        new_dict = {}

        for key, val in self.__objects.items():
            new_dict[key] = val.to_dict()

            with open(self.__file_path, "w", encoding="utf-8") as fobj:
                json.dump(new_dict, fobj, indent=2) #TO-DO remove the indent

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as pobj:
                py_obj = json.load(pobj)
                for values in py_obj.values():
                    cls_name = values["__class__"]
                    self.new(eval(cls_name)(**values))
