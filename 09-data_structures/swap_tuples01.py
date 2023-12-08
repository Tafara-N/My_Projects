#!/usr/bin/python3

'''Swapping tuples'''
a = 10
b = 15

print(f"Before swapping, a = {a} and b = {b}")
# swap the values of a and b
temp = a
a = b
b = temp

print(f"After swapping, a = {a} and b = {b}")

# but in python, using tuples make it easy to swap numbers
a, b = b, a
print(f"After swapping with tuples, a = {a} and b = {b}")
