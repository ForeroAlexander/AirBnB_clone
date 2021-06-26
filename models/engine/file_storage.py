#!/usr/bin/python3
""" create class FileStorage """

class FileStorage():
    __file_path = 'file.json'
    __objects = {}

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State


