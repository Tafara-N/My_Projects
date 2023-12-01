#!/usr/bin/python3

"""Prints each character in a string"""

f_name = input("first name:")

for c in f_name:
    print(c)

l_name = input("Surname:")

for c in l_name:
    if (c == "e"):
        continue
    print(c*3)
else:
    print("Finally loop finished executing.")
# remember the else staement is part of the loop
# so the else statement will not execute if you break out of the loop

# using the for loop in the range function 

for i in range(5):
    print(i)

# finding items with the for loop

name = input("Name:")

for f in name:
    if (f.lower() == "c"):
        print(f)
        break
else:
    print("Couldn't find what you were looking for.")
