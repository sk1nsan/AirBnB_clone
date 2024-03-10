#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import datetime
import unittest
import io
import os
from contextlib import redirect_stdout
import json


class TestFileStorage(unittest.TestCase):

    def test_all(self):
        storage = FileStorage()

        obj1 = User()
        storage.new(obj1)
        result = storage.all()
        self.assertEqual(result["User.{}".format(obj1.id)], obj1)

        obj2 = BaseModel()
        storage.new(obj2)
        result = storage.all()
        self.assertEqual(result["BaseModel.{}".format(obj2.id)], obj2)

        obj3 = State()
        storage.new(obj3)
        result = storage.all()
        self.assertEqual(result["State.{}".format(obj3.id)], obj3)

    def test_new(self):
        storage = FileStorage()

        obj4 = Amenity()
        storage.new(obj4)
        result = storage.all()
        self.assertEqual(result["Amenity.{}".format(obj4.id)], obj4)

        obj5 = City()
        storage.new(obj5)
        result = storage.all()
        self.assertEqual(result["City.{}".format(obj5.id)], obj5)

        obj6 = Place()
        storage.new(obj6)
        result = storage.all()
        self.assertEqual(result["Place.{}".format(obj6.id)], obj6)

        obj7 = Review()
        storage.new(obj7)
        result = storage.all()
        self.assertEqual(result["Review.{}".format(obj7.id)], obj7)

    def test_save(self):

        os.remove("file.json")

        file_storage = FileStorage()
        file_storage.reset()

        obj1 = BaseModel()
        obj2 = User()
        file_storage.new(obj1)
        file_storage.new(obj2)
        file_storage.save()

        with open("file.json", "r") as f:
            data = json.load(f)
            dict1 = obj1.to_dict()
            dict2 = obj2.to_dict()
            self.assertEqual(data["BaseModel.{}".format(obj1.id)], dict1)
            self.assertEqual(data["User.{}".format(obj2.id)], dict2)

    def test_reload(self):
        file_storage = FileStorage()

        obj1 = {
            "User.41bdd0dd-cac7-46ef-afdb-50b69e0f7fcd": {
                "id": "41bdd0dd-cac7-46ef-afdb-50b69e0f7fcd",
                "created_at": "2024-03-10T09:47:27.071747",
                "updated_at": "2024-03-10T09:47:27.071748",
                "__class__": "User",
            }
        }
        os.remove("file.json")
        file_storage.reset()

        with open("file.json", "w") as f:
            f.write(json.dumps(obj1))

        file_storage.reload()
        self.assertIn("User.41bdd0dd-cac7-46ef-afdb-50b69e0f7fcd",
                      file_storage.all().keys())

    def test_reset(self):

        file_storage = FileStorage()
        obj1 = BaseModel()
        file_storage.new(obj1)
        file_storage.save()
        self.assertGreater(len(file_storage.all()), 0)
        file_storage.reset()
        self.assertEqual(len(file_storage.all()), 0)
