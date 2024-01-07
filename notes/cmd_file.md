## Alternative Inputs:
## 1. Overview:
While the default mode for Cmd() involves interacting with the user through the readline library, it is also possible to pass a series of commands through standard input using Unix shell redirection.
## 2. Example Code:
import cmd

class HelloWorld(cmd.Cmd):

    # Disable rawinput module use
    use_rawinput = False

    # Do not show a prompt after each command read
    prompt = ''

    def do_greet(self, line):
        print("hello,", line)

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'rt') as input:
        HelloWorld(stdin=input).cmdloop()
# 3. Execution Example:
$ python3 cmd_file.py cmd_file.txt

hello,
hello, Alice and Bob
Explanation and Application to Airbnb Clone:
# Alternative Inputs:

This feature allows you to pass a series of commands through standard input, enabling non-interactive script execution.
Applying to Airbnb Clone:

You can create script files containing a sequence of commands that need to be executed in your Airbnb console.
For instance, you might have a script that initializes your database, sets up configurations, or performs other automated tasks.
Example Usage:

$ echo "help\ngreet Alice\nEOF" | python3 airbnb_console.py
This example sends a series of commands (help, greet Alice, and EOF) to the Airbnb console, allowing you to automate interactions.

Feel free to utilize this feature for automated testing, batch processing, or any scenario where scripted command execution is beneficial for your Airbnb project.
