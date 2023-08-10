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
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if name:
            if name in self.classes:
                Obj = eval(name)  # BaseModel
                mod = Obj()
                print("{}".format(mod.id))
                mod.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, str):
        """
        Prints the string representation of
        an instance based on the class name and id
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
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, str):
        """
        Deletes an instance based on the class name and id
        and saves the change into the JSON file
        """
        if str:
            tok = str.split()
            if tok[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(tok) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(tok[0], tok[1])
                objects = storage.all()
                if key in objects:
                    del objects[key]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, cmd_args):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        list_of_strings = []
        if not cmd_args:
            for key in storage.all():
                objects = str(storage.all()[key])
                list_of_strings.append(objects)
            
            print(list_of_strings)
        else:
            if cmd_args in self.classes:

                for key in storage.all():
                    class_name = key.split(".")

                    if class_name[0] == cmd_args:
                        objects = str(storage.all()[key])
                        list_of_strings.append(objects)

                print(list_of_strings)
            else:
                print("** class doesn't exist **")

    def do_update(self, cmd_args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute and save the change into the JSON file
        """
        if cmd_args:
            tok = cmd_args.split()
            if tok[0] in self.classes:
                if len(tok) < 2:
                    print("** instance id missing **")
                else:
                    key = "{}.{}".format(tok[0], tok[1])
                    if key in storage.all():
                        if len(tok) < 3:
                            print("** attribute name missing **")
                        elif len(tok) < 4:
                            print("** value missing **")
                        else:
                            # at this point args entered: update <class name> <id> <attribute name> name "<attribute value>"
                            # TO_DO: update attribute name with value it exists
                            # or add attribute name with value if it doesn't exist
                            pass
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
