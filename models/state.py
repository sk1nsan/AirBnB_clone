#!/usr/bin/python3

from models.base_model import BaseModel

""" State Class"""


class State(BaseModel):
    """State"""

    name = ""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
