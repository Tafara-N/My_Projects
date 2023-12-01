#!/usr/bin/python3

#Asks user for name and saves it in a variable
name = input("What is your name? ")

#make first letter a Block(upper)
i = 0
for c in name:
    if i == 0:
        c = c.upper()
        new_name = c
        i += 1
    else:
        c = c.lower()
        new_name += c

#prints users name to screen
print(f"{new_name}", end=" ")

#save the string length of name and save it in a variable
length = len(new_name)

#prints the length of the user's name
print(f"your name is {length} characters long")
