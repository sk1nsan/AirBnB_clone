#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

"""the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    """HBNBCommand"""

    prompt = "(hbnb) "
    classNames = ["BaseModel", "User", "State",
                  "City", "Amenity", "Place", "Review"]

    def emptyline(self):
        """empty lines enterned doesn't excute anything"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """help for quit"""
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """EOF exit the program"""
        return True

    def help_EOF(self):
        """help for EOF"""
        print("EOF exit the program\n")

    def do_create(self, arg):
        """Creates a new instance of given class,
        saves it (to the JSON file) and prints the id"""
        line = arg.split()
        if len(line) < 1:
            print("** class name missing **")
        elif line[0] not in HBNBCommand.classNames:
            print("** class doesn't exist **")
        else:
            b = eval("{}()".format(line[0]))
            storage.save()
            print(b.id)

    def help_create(self):
        """help for create"""
        print("Create a New instance of the given class")
        print("Usage: create <classname>\n")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        line = arg.split()
        if len(line) < 1:
            print("** class name missing **")
        elif line[0] not in HBNBCommand.classNames:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        elif line[0] + "." + line[1] not in storage.all().keys():
            print("** no instance found **")
        else:
            print(storage.all()[line[0] + "." + line[1]])

    def help_show(self):
        """help for show"""
        print("Prints the string representation of the given instance")
        print("Usage: show <classname> <instance id>\n")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        line = arg.split()
        if len(line) < 1:
            print("** class name missing **")
        elif line[0] not in HBNBCommand.classNames:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        elif line[0] + "." + line[1] not in storage.all().keys():
            print("** no instance found **")
        else:
            del storage.all()[line[0] + "." + line[1]]
            storage.save()

    def help_destroy(self):
        """help for destroy"""
        print("Prints the string representation of the given instance")
        print("Usage: destroy <classname> <instance id>\n")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        line = arg.split()
        instances = []
        if len(line) < 1:
            for value in storage.all().values():
                instances.append(str(value))
            print(instances)

        elif line[0] not in HBNBCommand.classNames:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if line[0] in key:
                    instances.append(str(value))
            print(instances)

    def help_all(self):
        """help for all"""
        print("Prints all string representation of all instances")
        print("Usage: all")
        print("Prints all string representation of specific class")
        print("Usage: all <classname>\n")

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        line = arg.split()
        if len(line) < 1:
            print("** class name missing **")
        elif line[0] not in HBNBCommand.classNames:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        elif line[0] + "." + line[1] not in storage.all().keys():
            print("** no instance found **")
        elif len(line) < 3:
            print("** attribute name missing **")
        elif len(line) < 4:
            print("** value missing **")
        else:
            obj = storage.all()[line[0] + "." + line[1]]
            setattr(obj, line[2], line[3][1:-1])
            # to fix The attribute value must be casted to the attribute type

    def help_update(self):
        """help for update"""
        print("Updates an instance based on the class name"
              " and id by adding or updating attribute")
        print("Usage: update <class name> <id>"
              " <attribute name> <attribute value>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()