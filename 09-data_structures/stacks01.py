#!/usr/bin/python3

'''
   Using lists as stacks
   A stack is a data structure that follows the LIFO principle
   that means last in, first out.
   we can use lists to implemet that
'''

'''We have the push: Adding an element to the top of the stack'''
stack = []
stack.append(1) # Pushes 1 onto the stack
stack.append(2) # Pushes 2 onto the stack

print(stack)

'''We have the pop: Removes and return the last element of a stack'''
item = stack.pop() # Removes the last if no index is passes to it
print(item)

'''Thus, this is a simple implemetation of stacks'''
