#!/usr/bin/python3
""" Create Class FileStorage """
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """Private class attributes for Class FileStorage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary with objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Returns __objects with obj set as key"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file inside"""
        new_dict = {}
        for key, item in FileStorage.__objects.items():
            new_dict[key] = item.to_dict().copy()
        with open(FileStorage.__file_path, mode="w") as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects
        only if the JSON file exists; otherwise, do nothing
        """
        try:
            with open(FileStorage.__file_path, mode="r") as file:
                new_dict = (json.load(file))
                for key, value in new_dict.items():
                    class_name = value.get('__class__')
                    obj = eval(class_name + '(**value)')
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
