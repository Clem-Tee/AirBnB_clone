#!/usr/bin/python3
"""Console"""

import cmd
import models


class HBNBCommand(cmd.Cmd):
    """HBNB console"""
    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
	"""Overwriting the emptyline method"""
	return False

    def do_quit(self, arg):
	"""Quit command to exit the program"""
	return True

    def do_create(self, arg):
	"""Creates a new instance of a class"""
	if len(args) == 0:
	    print("** class name missing **")
	    return False
	if args[0] in classes:
	    instance = classes[args[0]]()
	else:
	    print("**Class doesn't exist**")
	    return False
	print(instance.id)
	instance.save()

    def do_show(self, arg):
    """Prints an instance as string based on the class and id"""
	    if len(args) == 0;
	        print("** class name missing **")
		retun False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
