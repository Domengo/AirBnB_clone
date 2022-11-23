#!/usr/bin/python3
"""
class BaseModel defines all common attributes/methods for other classes
"""
from datetime import datetime
from uuid import uuid4

class BaseModel:
    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = uuid4().hex
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        class_name = self.__class__.__name__
        return f"[<{class_name}>] (<{self.id}>) <{self.__dict__}>"

    def save(self):
         self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
