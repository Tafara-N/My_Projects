#!/usr/bin/python3

"""Prints from 1 to 10"""

counter = 1 # Initialization

while (counter <= 10): # condition
    """WIll only execute if the condition is true"""
    if (counter == 4):
        print("four")
    elif (counter == 5):
        print("five")
    else:
        print(counter)

    counter = counter + 1 # increment/decrement

# the increment depends on the condtion you want to provide
print("Your loop finished executing")
