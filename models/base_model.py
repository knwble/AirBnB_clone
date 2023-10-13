#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4

""" This is the BaseModel file"""

class BaseModel():
    """
        This class defines all common attributes/methods for other classes
    """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        self.updated_at = datetime.now()
