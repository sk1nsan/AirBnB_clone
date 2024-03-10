#!/usr/bin/python3
"""unittesting Place Class"""

from models.place import Place
from models.base_model import BaseModel
import datetime
import unittest
import io
import os
from contextlib import redirect_stdout
import json


class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    def test_default_values(self):
        """Test default values"""
        place = Place()
        self.assertIsNotNone(place.id)
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)
        self.assertEqual(place.id, place.__dict__["id"])
        self.assertEqual(place.created_at, place.__dict__["created_at"])
        self.assertEqual(place.updated_at, place.__dict__["updated_at"])

    def test_save(self):
        """Test save method"""
        place = Place()
        place.city_id = "city123"
        place.user_id = "user456"
        place.name = "Cozy Cabin"
        place.description = "A cozy cabin in the woods."
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 123.456
        place.longitude = -78.910
        place.amenity_ids = ["amenity1", "amenity2"]
        old_updated_at = place.updated_at
        place.save()
        new_updated_at = place.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

        with open("file.json", "r") as f:
            data = json.load(f)
        id = place.id
        self.assertEqual(data["Place.{}".format(id)], place.to_dict())
        self.assertEqual(data["Place.{}".format(id)]["city_id"], "city123")
        self.assertEqual(data["Place.{}".format(id)]["user_id"], "user456")
        self.assertEqual(data["Place.{}".format(id)]["name"], "Cozy Cabin")
        self.assertEqual(
            data["Place.{}".format(place.id)]["description"],
            "A cozy cabin in the woods.",
        )
        self.assertEqual(data["Place.{}".format(id)]["number_rooms"], 2)
        self.assertEqual(data["Place.{}".format(id)]["number_bathrooms"], 1)
        self.assertEqual(data["Place.{}".format(id)]["max_guest"], 4)
        self.assertEqual(data["Place.{}".format(id)]["price_by_night"], 100)
        self.assertEqual(data["Place.{}".format(id)]["latitude"], 123.456)
        self.assertEqual(data["Place.{}".format(id)]["longitude"], -78.910)
        self.assertEqual(data["Place.{}".format(place.id)]["amenity_ids"],
                         ["amenity1", "amenity2"])

    def test_to_dict(self):
        """Test to_dict method"""
        place = Place()
        place.city_id = "city123"
        place.user_id = "user456"
        place.name = "Cozy Cabin"
        place.description = "A cozy cabin in the woods."
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 123.456
        place.longitude = -78.910
        place.amenity_ids = ["amenity1", "amenity2"]

        result = place.to_dict()

        self.assertIsInstance(result, dict)
        self.assertEqual(result["city_id"], "city123")
        self.assertEqual(result["user_id"], "user456")
        self.assertEqual(result["name"], "Cozy Cabin")
        self.assertEqual(result["description"], "A cozy cabin in the woods.")
        self.assertEqual(result["number_rooms"], 2)
        self.assertEqual(result["number_bathrooms"], 1)
        self.assertEqual(result["max_guest"], 4)
        self.assertEqual(result["price_by_night"], 100)
        self.assertEqual(result["latitude"], 123.456)
        self.assertEqual(result["longitude"], -78.910)
        self.assertEqual(result["amenity_ids"], ["amenity1", "amenity2"])
        self.assertEqual(result["__class__"], "Place")
        self.assertEqual(result["created_at"], place.created_at.isoformat())
        self.assertEqual(result["updated_at"], place.updated_at.isoformat())

    def test_str(self):
        """Test string representation"""
        place = Place()
        expected = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(str(place), expected)
