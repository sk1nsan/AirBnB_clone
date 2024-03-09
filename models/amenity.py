#!/usr/bin/python3

from models.base_model import BaseModel

""" Amenity Class"""


class Amenity(BaseModel):
    """Amenity"""

    name = ""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
