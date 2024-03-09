#!/usr/bin/python3
""" City Class"""


from models.base_model import BaseModel


class City(BaseModel):
    """City"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
