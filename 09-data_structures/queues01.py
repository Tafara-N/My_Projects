#!/usr/bin/python3

from collections import deque

'''
    Using lists as queues
    A queue is a data structure that follows the FIFO principle
    that means first in, first out
    we can use lists to implement that
 '''

'''We have the Enqueue: This adds an element to the back of a queue'''
queue = deque()
queue.append(1)  # Enqueues 1
queue.append(2)  # Enqueues 2
print(queue)

'''We had the Dequeue: This removes and returns the last element from the front of the queue'''
item = queue.popleft()  # Dequeues the first item (1)
print(item)
