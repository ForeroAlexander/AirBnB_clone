#!/usr/bin/python3
"""
Module Console
"""
import cmd
from os import linesep
from models import base_model
import models
from models.engine.file_storage import FileStorage
import shlex
import sys
import json
from models.base_model import BaseModel
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBcommand(cmd.Cmd):
    """ HBNB CLASS """
    prompt = '(hbnb)'

    classes = {'BaseModel': BaseModel, 'Amenity': Amenity,
               'State': State, 'Place': Place, 'Review': Review,
               'User': User, 'City': City}

    def do_EOF(self, args):
        """ End Of Line"""
        print()
        return True

    def do_quit(self, args):
        """ Close cmd """
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass

    def do_create(self, args):
        '''
        Create a new instance of class BaseModel and saves it
        to the JSON file.
        '''
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            args = shlex.split(args)
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

        except:
            print("** class doesn't exist **")

    def do_show(self, argument):
        """string view of id and class name"""
        tok = shlex.split(argument)
        if len(tok) == 0:
            print("** class name missing **")
        elif tok[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(tok) == 1:
            print("** instance id missing **")
        else:
            dic = models.storage.all()
            keyl = tok[0] + '.' + str(tok[1])
            if keyl in dic:
                print(dic[keyl])
            else:
                print("** no instance found **")
            return

    def do_destroy(self, argument):
        """delete string view of id and class name"""
        tok_del = shlex.split(argument)
        if len(tok_del) == 0:
            print("** class name missing **")
        elif tok_del[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(tok_del) == 1:
            print("** instance id missing **")
        else:
            dic = models.storage.all()
            k = tok_del[0] + '.' + (tok_del[1])
            if (k in dic):
                del dic[k]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, argument):
        """this function give us all string representation of all instances"""
        token_all = shlex.split(argument)
        list_all = []
        dic = models.storage.all()
        if len(token_all) == 0:
            for key in dic:
                representation_Class = str(dic[key])
                list_all.append(representation_Class)
            print(list_all)
            return

        if token_all[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            representation_Class = ""
            for key in dic:
                className = key.split('.')
                if className[0] == token_all[0]:
                    representation_Class = str(dic[key])
                    list_all.append(representation_Class)
            print(list_all)

    def do_update(self, args):
        '''
            Update an instance based on the class name and id
            sent as args.
        '''
        storage = FileStorage()
        storage.reload()
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        obj_dict = storage.all()
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(obj_value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()


if __name__ == "__main__":
    """Infinte loop"""
    HBNBcommand().cmdloop()
