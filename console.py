#!/usr/bin/env python3
"""
Contains the entry point of the command interpreter
"""


import cmd
import string
import sys
import string,sys
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    A command line interpreter that will be used as
    a console to interact with objects
    """
    def __init__(self):
        """
        Inserts (hbnb) as the prompt text
        """
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quits the program when you type quit or q
        """
        sys.exit(1)

    def do_EOF(self, arg):
        """
        Making the console program aware that no more input
        will be sent when you type EOF
        """
        return True

    def do_create(self, arg):
        """
        creates a new instance of BaseModel, saves it to the JSOn
        file and prints the id
        """
        temp = BaseModel()
        storage.save(temp)

    def emptyline(self):
        """
        Does nothing when no command is passed to the console or a return character or space
        is pressed
        """
        pass

    #shortcuts
    do_q = do_quit

    def do_create(self, line):
        """creates a new BaseModel instance
            line = args
        """
        if len(line) == 0:
            print('** class name missing **')
            return
        try:
            instance = line + "()"
            my_instance = eval(instance)
            my_instance.save()
            print(my_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):

        """Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234."""


if __name__ == "__main__":
    HBNBCommand().cmdloop()
