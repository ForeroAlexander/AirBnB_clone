#!/usr/bin/python3
"""
Module Console
"""
import cmd
import shlex
import sys
import models
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
      def do_EOF(self, argument):
            """ End Of Line"""
            print()
            return True
      def do_quit(self, argument):
            """ Close cmd """
            return True
if __name__ == "__main__":
      """Infinte loop"""
      HBNBcommand().cmdloop()
