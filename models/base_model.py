#!/usr/bin/python3
"""
class BaseModel defines all common attributes/methods for other classes
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""

        if kwargs.__len__() != 0:
            for key, values in kwargs.items():
                if key == "created_at" or key =="updated_at":
                    value = datetime.strptime(values, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                if key != "__class__":
                    setattr(self, key, values)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
