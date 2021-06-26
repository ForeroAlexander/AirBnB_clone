#!/usr/bin/python3
"""
Module Console
"""
import cmd
import shlex
import sys
import json
from models.base_model import BaseModel
from models import storage


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

      def do_show(self, args):
            '''
            Print the string representation of an instance baed on
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

      def do_all(self, line):
            """Prints all string representation of all instances.
            """
            if line != "":
                  words = line.split(' ')
                  if words[0] not in storage.classes():
                        print("** class doesn't exist **")
                  else:
                        l = [str(obj) for key, obj in storage.all().items()
                       if type(obj).__name__ == words[0]]
                  print(l)
            else:
                  l = [str(obj) for key, obj in storage.all().items()]
            print(l)

if __name__ == "__main__":
      """Infinte loop"""
      HBNBcommand().cmdloop()
