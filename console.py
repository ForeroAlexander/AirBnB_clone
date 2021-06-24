#!/usr/bin/python3
# comentrios

import cmd
from model.base_model import BaseModel

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
