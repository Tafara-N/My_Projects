## Configuring Cmd Through Attributes:
## 1. Overview:
In addition to methods, the cmd module provides attributes to configure the behavior of command interpreters. These attributes control aspects such as the prompt, welcome message, and formatting of help output.
## 2. Common Attributes:
prompt: This attribute sets the string to be printed each time the user is asked for a new command. You can dynamically change it within your program.

intro: The welcome message printed at the start of the program. It provides a friendly greeting or introduction to the user.

doc_header, misc_header, undoc_header: These attributes are used when printing help to format the output. They categorize commands into documented, miscellaneous, and undocumented.

ruler: The character used to create a ruler when printing help. It separates different sections of the help output.

## 3. Example Code:
import cmd

class HelloWorld(cmd.Cmd):

    prompt = 'prompt: '
    intro = "Simple command processor example."

    doc_header = 'doc_header'
    misc_header = 'misc_header'
    undoc_header = 'undoc_header'

    ruler = '-'

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ': '

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
## 4. Execution Example:
$ python3 cmd_attributes.py

Simple command processor example.
prompt: prompt hello
hello: help

doc_header
----------
help  prompt

undoc_header
------------
EOF

## hello:
Applying to Airbnb Clone:
You can use these attributes to enhance the user experience in your Airbnb console.
Set a clear and informative prompt to guide users.
Use intro to provide a warm welcome or instructions.
Customize headers (doc_header, misc_header, undoc_header) to make your help messages organized.
Choose a visually appealing ruler for separating sections in the help output.
For example, you might set the prompt to something like "Airbnb Console > " and use a comprehensive intro to guide users through the available commands.
