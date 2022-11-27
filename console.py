#!/usr/bin/env python3
"""
Contains the entry point of the command interpreter
"""


import cmd
import string
import sys


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

    # shortcuts
    do_q = do_quit


if __name__ == "__main__":
    HBNBCommand().cmdloop()
