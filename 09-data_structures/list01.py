#!/usr/bin/python3

'''
This is an implementation of list comprehension
this provides a concise way to create lists
They are a powerful tool for creating new lists
by applying an expression to each item in an existing iterable.
'''

# Without list comprehension
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)

# Using list comprehension
squares = [i ** 3 for i in range(10)] # We can use lambda here
print(squares)
