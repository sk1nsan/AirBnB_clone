#!/usr/bin/python3
""" State Class"""


from models.base_model import BaseModel


class State(BaseModel):
    """State"""

    name = ""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
