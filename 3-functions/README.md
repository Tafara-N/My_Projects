# Functions

In Python, a function is a block of reusable code that performs a specific task or set of tasks. Functions help in organizing code into modular and manageable pieces, making it easier to understand, reuse, and maintain. Here's a breakdown of key concepts related to functions in Python:

## Function Definition:

def function_name(parameters):
    # Code block
    # ...
    return result  # Optional return statement
def: Keyword used to define a function.
function_name: Name of the function, following the same naming rules as variables.
parameters: Input values that the function takes (if any).
:: Colon indicates the beginning of the function body.
## Function Call:

result = function_name(arguments)
function_name: The name of the function being called.
arguments: Actual values passed to the function's parameters.
## Example:

def add_numbers(x, y):
    result = x + y
    return result

sum_result = add_numbers(3, 5)
print(sum_result)  # Output: 8
## Return Statement:
Functions can use the return statement to send a value back to the caller.
If there's no return statement, the function returns None by default.
## Default Parameters:

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")          # Output: Hello, Alice!
greet("Bob", "Hi")      # Output: Hi, Bob!
## Default values for parameters are specified in the function definition.
If a value is provided for a parameter during the function call, it overrides the default.
Variable Scope:
Variables defined inside a function are usually local to that function.
Variables defined outside any function are global.
Global variables can be accessed within a function, but to modify them, you need to use the global keyword.
## Docstrings:
It's good practice to include documentation (docstring) in triple-quotes immediately after the function definition to describe its purpose, parameters, and return values.
## Lambda Functions (Anonymous Functions):

multiply = lambda x, y: x * y
result = multiply(3, 4)
print(result)  # Output: 12
A lambda function is a concise way to create small anonymous functions.
They are often used for short-term operations.
Functions in Python provide a powerful mechanism for code organization, reusability, and abstraction, contributing to the overall readability and maintainability of your code

![SHHSS](https://happycoding.io/tutorials/html/images/rainbow-logo-2.png)

