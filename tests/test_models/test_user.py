#!/usr/bin/python3

from models.user import User
from models.base_model import BaseModel
import datetime
import unittest
import io
import os
from contextlib import redirect_stdout
import json


class TestUser(unittest.TestCase):

    def test_default_values(self):
        """Test default values"""
        user = User()
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_to_dict(self):
        """Test to_dict method"""
        user = User()
        user.email = "example@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        user_dict = user.to_dict()

        self.assertEqual(user_dict["email"], "example@example.com")
        self.assertEqual(user_dict["password"], "password123")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")

    def test_str(self):
        """Test string representation"""
        user = User()
        expected = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected)

    def test_save(self):
        """Test save method"""
        user = User()
        user.email = "test@example.com"
        user.password = "test123"
        user.first_name = "John"
        user.last_name = "Doe"

        old_updated_at = user.updated_at
        user.save()
        new_updated_at = user.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

        with open("file.json", "r") as f:
            data = json.load(f)

        user_key = "User.{}".format(user.id)
        self.assertTrue(user_key in data)
        self.assertEqual(data[user_key]["email"], "test@example.com")
        self.assertEqual(data[user_key]["password"], "test123")
        self.assertEqual(data[user_key]["first_name"], "John")
        self.assertEqual(data[user_key]["last_name"], "Doe")
