#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print()
print()

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
print()
print()

print("-- Create another new object --")
my_model_2 = BaseModel()
my_model_2.name = "My_Second_Model"
my_model_2.my_number = 90
my_model_2.save()
print(my_model_2)
