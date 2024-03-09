#!/usr/bin/python3

from models.base_model import BaseModel

""" City Class"""


class City(BaseModel):
    """City"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
