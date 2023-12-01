#!/usr/bin/python3

# The "and" keyword is a logical operator, and is used to combine conditional statements:
# Test if a is greater than b, AND if c is greater than a:
a = 200
b = 50
c = 300
if a > b and c > a:
    print("Both conditions are true")

# The or keyword is a logical operator, and is used to combine conditional statements:
# Test if a is greater than b, OR if a is greater than c:
a = 200
b = 300
c = 50
if a > b or a > c:
    print("At least one of the conditons is true")

# Test if a is NOT greater than b:
a = 33
b = 200
if not a > b:
    print("A is not greater than B")

# You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
    print("x is above 10")
    if x > 20:
        print("and above 20")
        if x > 30:
            print("and also above 30")
    else:
        print("but not above 20")

# if statements cannot be empty,
# but if you for some reason have an if statement with no content
# put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass
