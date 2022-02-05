#!/usr/bin/python3
"""Console"""

import cmd
import models


class HBNBCommand(cmd.Cmd):
    """ HBNB console """
    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
	""" overwriting the emptyline method """
	return False

    def do_quit(self, arg):
	"""Quit command to exit the program"""
	return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
