#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from . import storage

""" BaseModel Class"""


class BaseModel:
    """BaseModel"""

    def __init__(self, *args, **kwargs):
        """init method"""
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.fromisoformat(v))
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """string representation which is in this format
         [<class name>] (<self.id>) <self.__dict__>"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at and saves it"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing
         all keys/values of __dict__ of the instance"""
        copy_dict = self.__dict__.copy()
        copy_dict["__class__"] = self.__class__.__name__
        copy_dict["created_at"] = self.created_at.isoformat()
        copy_dict["updated_at"] = self.updated_at.isoformat()
        return copy_dict
