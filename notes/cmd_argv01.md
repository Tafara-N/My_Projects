## Now, Let's explore processing commands from sys.argv in the cmd module:

## Commands from sys.argv:
# 1. Overview:
Command line arguments to the program can be processed as commands for the Cmd interpreter class, allowing for more flexibility in program execution.
# 2. Example Code:
import cmd

class InteractiveOrCommandLine(cmd.Cmd):
    """Accepts commands via the normal interactive
    prompt or on the command line.
    """

    def do_greet(self, line):
        print('hello,', line)

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        InteractiveOrCommandLine().onecmd(' '.join(sys.argv[1:]))
    else:
        InteractiveOrCommandLine().cmdloop()
# 3. Execution Examples:
$ python3 cmd_argv.py greet Command-Line User

hello, Command-Line User
$ python3 cmd_argv.py

(Cmd) greet Interactive User
hello, Interactive User
(Cmd)
## Explanation and Application to Airbnb Clone:
# Commands from sys.argv:

This feature allows you to process command line arguments as commands for the Cmd interpreter class.
The onecmd() method is used to directly execute commands passed through the command line.
Applying to Airbnb Clone:

You can leverage this feature to automate specific actions or tasks when launching your Airbnb console.
For instance, you might have a script that initializes the application with specific configurations or performs a quick check on the system.
# Example Usage:

$ python3 airbnb_console.py initialize
This example launches the Airbnb console and executes the initialize command, triggering actions associated with initializing the application.

Feel free to utilize this approach to streamline your workflow or automate common tasks when interacting with your Airbnb console.
