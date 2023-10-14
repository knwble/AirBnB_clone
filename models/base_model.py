#!/usr/bin/python3
"""This python script is the base model"""

import uuid
from datetime import datetime


class BaseModel():

    """This class defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """ initializes a new BaseModel

        Args:
            *args: List of arguments (not used)
            **kwargs: Dictionary of key-value arguments

        """

        if kwargs is not None and kwargs != {}::
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["update    d_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Returns String Representation """

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the public instance attribute update_at """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ """

        mydict = self.__dict__.copy()
        mydict["__class__"] = type(self).__name__
        mydict["created_at"] = mydict["created_at"].isoformat()
        mydict["updated_at"] = mydict["updated_at"].isoformat()
        return mydict
