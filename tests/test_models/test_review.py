#!/usr/bin/python3
"""unittesting Review Class"""

from models.review import Review
from models.base_model import BaseModel
import datetime
import unittest
import io
import os
from contextlib import redirect_stdout
import json


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_default_values(self):
        """Test default values"""
        review = Review()
        self.assertIsNotNone(review.id)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)
        self.assertEqual(review.id, review.__dict__["id"])
        self.assertEqual(review.created_at, review.__dict__["created_at"])
        self.assertEqual(review.updated_at, review.__dict__["updated_at"])

    def test_save(self):
        """Test save method"""
        review = Review()
        review.place_id = "place123"
        review.user_id = "user456"
        review.text = "This is a review."
        old_updated_at = review.updated_at
        review.save()
        new_updated_at = review.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

        with open("file.json", "r") as f:
            data = json.load(f)
        self.assertEqual(data["Review.{}".format(review.id)],
                         review.to_dict())
        self.assertEqual(data["Review.{}".format(review.id)]["place_id"],
                         "place123")
        self.assertEqual(data["Review.{}".format(review.id)]["user_id"],
                         "user456")
        self.assertEqual(data["Review.{}".format(review.id)]["text"],
                         "This is a review.")

    def test_to_dict(self):
        """Test to_dict method"""
        review = Review()
        review.place_id = "place123"
        review.user_id = "user456"
        review.text = "This is a review."

        result = review.to_dict()

        self.assertIsInstance(result, dict)
        self.assertEqual(result["place_id"], "place123")
        self.assertEqual(result["user_id"], "user456")
        self.assertEqual(result["text"], "This is a review.")
        self.assertEqual(result["__class__"], "Review")
        self.assertEqual(result["created_at"], review.created_at.isoformat())
        self.assertEqual(result["updated_at"], review.updated_at.isoformat())

    def test_str(self):
        """Test string representation"""
        review = Review()
        expected = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(str(review), expected)
