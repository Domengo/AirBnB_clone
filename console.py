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

    def emptyline(self):
        """
        Does nothing when no command is passed to the console or a return character or space
        is pressed
        """
        pass

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

        """
        Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 49faff9a-6318-451f-87b6-910505c55907
        prints [BaseModel] (49faff9a-6318-451f-87b6-910505c55907) 
        {
        'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 
        'id': '49faff9a-6318-451f-87b6-910505c55907', 
        'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)
        }
        """
        try:
            lst = line.split()
            if len(lst) == 0:
                print("** class name missing **")
                return
            for key, value in models.storage.all().items():
                if len(lst) == 2:
                    if key == f"{lst[0]}.{lst[1]}":
                        print(value)
                        return
                if len(lst) == 1:
                    if key.split(".")[0] != lst[0]:
                        print("** class doesn't exist **")
                        return
                    if key.split(".")[0] == lst[0]:
                        print("** instance id missing **")
                        return
            print("** no instance found **")
            return
        except Exception as excp:
            print(excp)

    def do_destroy(self, line):
        """
        Deletes an instance base on the class name and id
        Ex: (hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
            (hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
        ** no instance found **
        """
        try:
            lst = line.split()
            if len(lst) == 0:
                print("** class name missing **")
                return
            for key, value in models.storage.all().items():
                if len(lst) == 2:
                    if key == f"{lst[0]}.{lst[1]}":
                        models.storage.all().pop(key)
                        models.storage.save()
                        return
                if len(lst) == 1:
                    if key.split(".")[0] != lst[0]:
                        print("** class doesn't exist **")
                        return
                    if key.split(".")[0] == lst[0]:
                        print("** instance id missing **")
                        return
            print("** no instance found **")
            return
        except Exception as excp:
            print(excp)

    def do_all(self, line):
        """
        Prints all the string representation of all instances based 
        or not on the class name
        Ex: (hbnb) all BaseModel
            ["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) 
            {
            'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 
            'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 
            'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)
            }",
            "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) 
            {
            'id': '49faff9a-6318-451f-87b6-910505c55907', 
            'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 
            'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)
            }
            "]
        """
        lst = line.split()
        for key, value in models.storage.all().items():
            if len(lst) == 0:
                print(value)
                continue
            if len(lst) == 1:
                if key.split(".")[0] != lst[0]:
                    print("** class doesn't exist **")
                    return
                if key.split(".")[0] == lst[0]:
                    print(value)

    #shortcuts
    do_q = do_quit
    do_c = do_create
    do_s = do_show
    do_d = do_destroy

if __name__ == "__main__":
    HBNBCommand().cmdloop()
