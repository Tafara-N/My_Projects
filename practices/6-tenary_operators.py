#!/usr/bin/python3

""""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""
# These conditions can be used in several ways, most commonly in "if statements" and loops.

# if statement
a = 33
b = 200
if b > a:
    print("b is greater than a")


# take notice of the use of indentation
# without proper indentation, we will get an error
# unlikeother programming languages that use braces, python uses indentations

# elif / else if statments
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# else statement
# The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b")
    
# You can also have an else without the elif:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# One line if statement:
if a > b: print("a is greater than b")

# One line if else statement:
a = 2
b = 330
print("A") if a > b else print("B")

# You can also have multiple else statements on the same line:
a = 200
b = 200
print("A") if a > b else print("=") if a == b else print("B")
