#!/usr/bin/python3

from models.base_model import BaseModel

""" Review Class"""


class Review(BaseModel):
    """Review"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
