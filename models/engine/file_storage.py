#!/usr/bin/python3
"""Define file storage class to store objects
"""
from models.base_model import BaseModel
import os
import json


class FileStorage():
    """Defines method and attribute for file storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all elements in storage
        """
        return FileStorage.__objects

    def new(self, obj):
        """Add new object to storage
        """
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Save items to file storage
        """
        mydict = {}
        for key, value in FileStorage.__objects.items():
            mydict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as myfile:
            json.dump(mydict, myfile)

    def reload(self):
        """Load items from file storage
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as myfile:
                mydict = json.load(myfile)
                for key, value in mydict.items():
                    classname = value['__class__']
                    class_obj = eval(classname)
                    myobj = class_obj(**value)
                    self.new(myobj)
