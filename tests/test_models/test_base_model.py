#!/usr/bin/python3
"""Unittesting BaseModel"""
from models.base_model import BaseModel
import datetime
import unittest
import io
import os
from contextlib import redirect_stdout
import json


class TestBaseModel(unittest.TestCase):
    """ BaseModel Test Class"""

    # BaseModel instance is created successfully with default values
    def test_default_values(self):
        """test init method"""
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)
        self.assertEqual(model.id, model.__dict__["id"])
        self.assertEqual(model.created_at, model.__dict__["created_at"])
        self.assertEqual(model.updated_at, model.__dict__["updated_at"])

        model2 = BaseModel()
        model2.number = 10
        dict = model2.to_dict()
        model3 = BaseModel(**dict)
        self.assertEqual(model3.number, 10)
        self.assertEqual(model2.id, model3.id)
        self.assertEqual(model2.created_at, model3.created_at)
        self.assertEqual(model2.updated_at, model3.updated_at)
        self.assertIsNot(model2, model3)

    def test_save(self):
        """test save method"""
        obj = BaseModel()
        obj.number = 10
        old_updated_at = obj.updated_at
        obj.save()
        new_updated_at = obj.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

        with open("file.json", "r") as f:
            json_file = json.loads(f.read())
        self.assertEqual(json_file["BaseModel.{}".format(obj.id)], obj.to_dict())
        self.assertEqual(json_file["BaseModel.{}".format(obj.id)]["number"], 10)

    def test_to_dict(self):
        """" test to_dict method"""
        obj = BaseModel()

        obj.name = "John"
        obj.age = 25

        result = obj.to_dict()

        self.assertIsInstance(result, dict)

        self.assertEqual(result["name"], "John")
        self.assertEqual(result["age"], 25)
        self.assertEqual(result["__class__"], "BaseModel")
        self.assertEqual(result["created_at"], obj.created_at.isoformat())
        self.assertEqual(result["updated_at"], obj.updated_at.isoformat())

    def test_str(self):
        """test string rerpresentaion"""
        obj = BaseModel()
        expected = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected)
