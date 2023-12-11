#!/usr/bin/python3
""" This Module defines the Base Model Class
"""
import json
import uuid
from datetime import datetime
import models


class BaseModel():
    """ Defines common Attributes
    and methods for other classes
    """

    id = ""
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs):
        """ Initialize values
        for object creation
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        String representation of object
        """
        return ("[{}] ({}) {}".format(type(self).__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Saves Object to storage
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dictionary representation of object
        """
        mydict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                mydict[key] = value.isoformat()
            else:
                mydict[key] = value
        return {
                **mydict,
                '__class__': type(self).__name__
                }
