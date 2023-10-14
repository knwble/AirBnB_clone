#!/usr/bin/python3
"""This program contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):

    """the command line interpreter class"""

    prompt = "(hbnh) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Handles EOF"""
        print()
        return True

    def emptyline(self):
        """Does not execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
