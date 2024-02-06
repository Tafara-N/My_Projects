#!/usr/bin/python3

import cmd
import json

class UserManagement(cmd.Cmd):
    """simple CRUD command for managing users"""

    prompt = "shell $ "
    def __init__(self):
        super().__init__()
        self.users = {} #dictionary to store users
        
    def do_create(self, line):
        """create a new user Syntax: create <digit> <name>"""
        args = line.split()
        if len(args) == 2:
            digit, name = args
            self.users[digit] = name
            print(f"User created - ID: {digit}, Name: {name}")
        else:
            print("Invalid input. Use: create <digit> <name>")
        self.save_to_file()

    def do_read(self, line):
        """Read and Display all users"""
        self.load_from()
        print("list of users:")
        for digit, name in self.users.items():
            print(f"ID: {digit} -> Name: {name}")

    def do_update(self, line):
        """UPdate user's name. Syntax: update <digit> <name>"""
        args = line.split()
        if len(args) == 2:
            digit, name = args
            if digit in self.users:
                self.users[digit] = name
                print(f"User update - ID: {digit}, Name: {name}")
            else:
                print(f"No user found with - ID {digit}")
        else:
            print("Invalid input. Use: update <digit> <name>")
        self.save_to_file()

    def do_destroy(self, line):
        """Delete a User by ID. Syntax: update <digit> <name> """
        if line in self.users:
            del self.users[line]
            print(f"User deleted - ID: {line}")
        else:
            print(f"No user found with ID {line}")
        self.save_to_file()

    def save_to_file(self):
        """save data to file"""
        with open("user_data.json", "a") as json_file:
            json.dump(self.users, json_file)

    def load_from(self):
        """loads the user data from the json file"""
        with open("user_data.json", "r") as json_file:
            self.users = json.load(json_file)

            # print(self.users["4"])
    

if __name__ == '__main__':
    UserManagement().load_from()
    UserManagement().cmdloop()
