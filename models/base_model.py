#!/usr/bin/python3
"""
class BaseModel defines all common attributes/methods for other classes
"""
import datetime
import uuid
import time

class BaseModel:
    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = uuid.uuid4().hex
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
    
    def __str__(self):
        class_name = self.__class__.__name__
        return f"[<{class_name}>] (<{self.id}>) <{self.__dict__}>"

    def save(self):
         self.updated_at = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S    .%f")

    def to_dict(self):
        return self.__all__.__dict__.items()
