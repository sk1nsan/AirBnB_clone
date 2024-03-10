#!/usr/bin/python3
"""unittesting Amenity Class"""

from models.amenity import Amenity
from models.base_model import BaseModel
import datetime
import unittest
import io
import os
from contextlib import redirect_stdout
import json


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_default_values(self):
        """Test default values"""
        amenity = Amenity()
        self.assertIsNotNone(amenity.id)
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)
        self.assertEqual(amenity.id, amenity.__dict__["id"])
        self.assertEqual(amenity.created_at, amenity.__dict__["created_at"])
        self.assertEqual(amenity.updated_at, amenity.__dict__["updated_at"])

    def test_save(self):
        """Test save method"""
        amenity = Amenity()
        amenity.name = "Wi-Fi"
        old_updated_at = amenity.updated_at
        amenity.save()
        new_updated_at = amenity.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

        with open("file.json", "r") as f:
            data = json.load(f)
        id = amenity.id
        self.assertEqual(data["Amenity.{}".format(id)], amenity.to_dict())
        self.assertEqual(data["Amenity.{}".format(id)]["name"], "Wi-Fi")

    def test_to_dict(self):
        """Test to_dict method"""
        amenity = Amenity()
        amenity.name = "Wi-Fi"

        result = amenity.to_dict()

        self.assertIsInstance(result, dict)
        self.assertEqual(result["name"], "Wi-Fi")
        self.assertEqual(result["__class__"], "Amenity")
        self.assertEqual(result["created_at"], amenity.created_at.isoformat())
        self.assertEqual(result["updated_at"], amenity.updated_at.isoformat())

    def test_str(self):
        """Test string representation"""
        amenity = Amenity()
        expected = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected)
