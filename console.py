#!/usr/bin/python3
"""Module defines console CLI for
HBNB APP
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Creates a CLI for HBNB
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command exits the program
        """
        return True

    def do_EOF(self, line):
        """EOF command exits the program
        """
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates an object of specified class
        Ex: $ create BaseModel
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        else:
            try:
                myobj = eval(args[0])()
            except Exception:
                print(f"** class doesn't exist **")
            else:
                storage.new(myobj)
                storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance
        Ex: $ show BaseModel 1234-1234-1234
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            allobjs = storage.all()
            classfound = 0
            for value in allobjs.values():
                mydict = value.to_dict()
                if mydict['__class__'] == args[0]:
                    classfound = 1
            if classfound:
                key = f"{args[0]}.{args[1]}"
                try:
                    myobj = allobjs[key]
                except Exception:
                    print("** no instance found **")
                else:
                    print(myobj)
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes instance based on class and id
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            allobjs = storage.all()
            classfound = 0
            for value in allobjs.values():
                mydict = value.to_dict()
                if mydict['__class__'] == args[0]:
                    classfound = 1
            if classfound:
                key = f"{args[0]}.{args[1]}"
                try:
                    del storage.all()[key]
                except Exception:
                    print("** no instance found **")
                else:
                    storage.save()
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances
        Ex: $ all BaseModel or $ all
        """
        args = line.split()
        allobjs = storage.all()
        mylist = []
        if len(args) > 0:
            classfound = 0
            for value in allobjs.values():
                myobj = value.to_dict()
                if myobj['__class__'] == args[0]:
                    classfound = 1
                    del myobj['__class__']
                    mylist.append(str(myobj))
            if classfound:
                print(mylist)
            else:
                print("** class doesn't exist **")
        else:
            for value in allobjs.values():
                myobj = value.to_dict()
                del myobj['__class__']
                mylist.append(str(myobj))
            print(mylist)

    def do_update(self, line):
        """Updates instance attriutes
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            allobjs = storage.all()
            classfound = 0
            for value in allobjs.values():
                mydict = value.to_dict()
                if mydict['__class__'] == args[0]:
                    classfound = 1
            if classfound:
                key = f"{args[0]}.{args[1]}"
                try:
                    myobj = allobjs[key]
                except Exception:
                    print("** no instance found **")
                else:
                    setattr(storage.all()[key], args[2], args[3])
                    storage.save()
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
