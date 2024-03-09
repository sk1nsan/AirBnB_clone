#!/usr/bin/python3
""" Amenity Class"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity"""

    name = ""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
