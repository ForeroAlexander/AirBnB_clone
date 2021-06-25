#!/usr/bin/python3
"""
Module Console
"""
import cmd
import shlex
import sys
import models
import json
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
      def do_EOF(self, args):
            """ End Of Line"""
            print()
            return True
      def do_quit(self, args):
            """ Close cmd """
            return True
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

      def do_show(self, args):
            '''
            Print the string representation of an instance based on
            the class name and id given as args.
            '''
            args = shlex.split(args)
            if len(args) == 0:
                  print("** class name missing **")
                  return
            if len(args) == 1:
                  print("** instance id missing **")
                  return
      storage = FileStorage()
      storage.reload()
      obj_dict = storage.all()
      try:
            eval(args[0])
      except NameError:
            print("** class doesn't exist **")
            return
      key = args[0] + "." + args[1]
      key = args[0] + "." + args[1]
      try:
            value = obj_dict[key]
            print(value)
      except KeyError:
            print("** no instance found **")

if __name__ == "__main__":
      """Infinte loop"""
      HBNBcommand().cmdloop()
