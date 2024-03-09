#!/usr/bin/python3
"""Unittesting BaseModel"""
from models.base_model import BaseModel
import datetime
import unittest


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

    def test_save(self):
        """test save method"""
        pass

    def test_to_dict(self):
        """" test to_dict method"""
        pass

    def test_str(self):
        """test string rerpresentaion"""
        pass
