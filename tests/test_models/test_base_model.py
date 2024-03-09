#!/usr/bin/python3
"""Unittesting BaseModel"""
from models.base_model import BaseModel
import datetime
import unittest


class TestBaseModel(unittest.TestCase):

    # BaseModel instance is created successfully with default values
    def test_default_values(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)
        self.assertEqual(model.id, model.__dict__["id"])
        self.assertEqual(model.created_at, model.__dict__["created_at"])
        self.assertEqual(model.updated_at, model.__dict__["updated_at"])
