#!/usr/bin/python3
import os
import json

""" FileStorage Class"""


class FileStorage:
    """FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        which store all objects by <class name>.id"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        className = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(className, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w") as f:
            f.write(
                json.dumps(
                    {
                        key: value.to_dict()
                        for key, value in FileStorage.__objects.items()
                    }
                )
            )

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review

            with open(self.__file_path, "r") as f:
                dict = json.loads(f.read())
                for key, value in dict.items():
                    class_name = value["__class__"]
                    obj = eval("{}(**value)".format(class_name))
                    FileStorage.__objects[key] = obj
