#!/usr/bin/python3
""" User Class"""


from models.base_model import BaseModel


class User(BaseModel):
    """User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
