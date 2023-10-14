#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4

""" This is the BaseModel file"""

class BaseModel():
    """
        This class defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """ initializes a new BaseModel

        Args:
        *args: List of arguments (not used)
        **kwargs: Dictionary of key-value arguments

        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
            self.id = kwargs.get("id", str(uuid4()))

        else:

            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Returns String Representation """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the public instance attribute update_at """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ """

        mydict = self.__dict__.copy()
        mydict["__class__"] = self.__class__.__name__
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        return mydict
