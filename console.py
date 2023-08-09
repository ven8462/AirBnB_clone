#!/usr/bin/python3
"""commandline interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """creates an entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """quits the console"""
        return True

    def do_EOF(self, line):
        """quits non_interactive part"""
        return True

    def emptyline(self):
        """does nothing on emptyline"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
