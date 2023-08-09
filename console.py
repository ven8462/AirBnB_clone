#!/usr/bin/python3
"""
Command-line interpreter module
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Creates an entry point of the command interpreter
    """
    prompt = "(hbnb) "
    classes = ("BaseModel")

    def do_quit(self, line):
        """
        Command to exit the console
        """
        return True

    def do_EOF(self, line):
        """
        Command to exit the console
        """
        return True

    def emptyline(self):
        """
        Command to do nothing when newline is entered
        """
        return

    def do_create(self, name):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        if name:
            if name in self.classes:
                Obj = eval(name) # BaseModel
                mod = Obj()
                print("{}".format(mod.id))
                mod.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, str):
        """
        Prints the string representation of an instance based on the class name and id
        """
        if str:
            tok = str.split()
            if tok[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(tok) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(tok[0], tok[1])
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
