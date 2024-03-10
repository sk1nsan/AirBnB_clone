#!/usr/bin/python3
"""unittesting City Class"""

from models.city import City
from models.base_model import BaseModel
import datetime
import unittest
import io
import os
from contextlib import redirect_stdout
import json


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_default_values(self):
        """Test default values"""
        city = City()
        self.assertIsNotNone(city.id)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)
        self.assertEqual(city.id, city.__dict__["id"])
        self.assertEqual(city.created_at, city.__dict__["created_at"])
        self.assertEqual(city.updated_at, city.__dict__["updated_at"])

    def test_save(self):
        """Test save method"""
        city = City()
        city.state_id = "state123"
        city.name = "San Francisco"
        old_updated_at = city.updated_at
        city.save()
        new_updated_at = city.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

        with open("file.json", "r") as f:
            data = json.load(f)
        id = city.id
        self.assertEqual(data["City.{}".format(id)], city.to_dict())
        self.assertEqual(data["City.{}".format(id)]["state_id"], "state123")
        self.assertEqual(data["City.{}".format(id)]["name"], "San Francisco")

    def test_to_dict(self):
        """Test to_dict method"""
        city = City()
        city.state_id = "state123"
        city.name = "San Francisco"

        result = city.to_dict()

        self.assertIsInstance(result, dict)
        self.assertEqual(result["state_id"], "state123")
        self.assertEqual(result["name"], "San Francisco")
        self.assertEqual(result["__class__"], "City")
        self.assertEqual(result["created_at"], city.created_at.isoformat())
        self.assertEqual(result["updated_at"], city.updated_at.isoformat())

    def test_str(self):
        """Test string representation"""
        city = City()
        expected = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected)
