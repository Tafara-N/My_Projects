#!/usr/bin/python3

import cmd

class command(cmd.Cmd):

	"""a simple command line interpreter"""

	def do_greet(self, line):
		print("Hello world")

	def do_EOF(self, line):
		print()
		return True

	def default(self, line):
		print(f"Unknown command: {line}")

if __name__ == '__main__':
	command().cmdloop()
