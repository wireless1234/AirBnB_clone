#!/usr/bin/python3
"""
"""
from models.base_model import BaseModel
import os
import json


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        mydict = {}
        for key, value in FileStorage.__objects.items():
            mydict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as myfile:
            json.dump(mydict, myfile)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as myfile:
                mydict = json.load(myfile)
                for key, value in mydict.items():
                    classname = value['__class__']
                    class_obj = eval(classname)
                    myobj = class_obj(**value)
                    self.new(myobj)
