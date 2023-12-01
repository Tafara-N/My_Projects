#!/usr/bin/python3

"""Give us directions based on traffic rules"""

# Ask for colour
colour_input = input("What is the colour of the light? ")

colour = colour_input.lower()

if (colour == "red"):
    print("STOP !!!")
elif (colour == "yellow"):
    print("Get ready !!!")
elif (colour == "green"):
    print("GO !!!")
else:
    print("invalid colour")
