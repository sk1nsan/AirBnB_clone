#!/usr/bin/python3
"""unittesting State"""

from models.state import State
from models.base_model import BaseModel
import datetime
import unittest
import io
import os
from contextlib import redirect_stdout
import json


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_default_values(self):
        """Test default values"""
        state = State()
        self.assertIsNotNone(state.id)
        self.assertIsNotNone(state.created_at)
        self.assertIsNotNone(state.updated_at)
        self.assertEqual(state.id, state.__dict__["id"])
        self.assertEqual(state.created_at, state.__dict__["created_at"])
        self.assertEqual(state.updated_at, state.__dict__["updated_at"])

    def test_save(self):
        """Test save method"""
        state = State()
        state.name = "Alaska"
        old_updated_at = state.updated_at
        state.save()
        new_updated_at = state.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

        with open("file.json", "r") as f:
            data = json.load(f)
        self.assertEqual(data["State.{}".format(state.id)], state.to_dict())
        self.assertEqual(data["State.{}".format(state.id)]["name"], "Alaska")

    def test_to_dict(self):
        """Test to_dict method"""
        state = State()
        state.name = "California"

        result = state.to_dict()

        self.assertIsInstance(result, dict)
        self.assertEqual(result["name"], "California")
        self.assertEqual(result["__class__"], "State")
        self.assertEqual(result["created_at"], state.created_at.isoformat())
        self.assertEqual(result["updated_at"], state.updated_at.isoformat())

    def test_str(self):
        """Test string representation"""
        state = State()
        expected = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), expected)
