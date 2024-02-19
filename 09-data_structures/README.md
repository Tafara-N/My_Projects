# Lists:

Ordered collection of items.
Mutable (can be modified).
Example:

my_list = [1, 2, 3, 'a', 'b']

## Tuples:

Similar to lists but immutable (cannot be modified once created).
Example:

my_tuple = (1, 2, 3, 'a', 'b')
Sets:

Unordered collection of unique items.
Mutable.
Example:

my_set = {1, 2, 3, 'a', 'b'}
Dictionaries:

Collection of key-value pairs.
Mutable.
Example:

my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
Stacks:

Last In, First Out (LIFO) structure.
Can be implemented using lists.
## Example:

stack = []
stack.append(1)
stack.append(2)
stack.pop()  # Removes and returns the last element (2)

## Queues:

First In, First Out (FIFO) structure.
Can be implemented using lists or the queue module.
Example:

from queue import Queue
my_queue = Queue()
my_queue.put(1)
my_queue.put(2)
my_queue.get()  # Removes and returns the first element (1)

## Linked Lists:

Series of elements, each pointing to the next.
Implemented using custom classes.
## Example:

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
## Trees:

Hierarchical data structure.
Consists of nodes with a parent-child relationship.

## Example: Binary Tree
class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
Graphs:

## Collection of nodes and edges.
Can be represented using adjacency lists or matrices.
## Example:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    # ...
}

## Heaps:

Specialized tree-based data structure.
Binary heap is common (min-heap or max-heap).
Implemented using lists.

## Example:
import heapq
heap = [3, 1, 4, 1, 5, 9, 2]
heapq.heapify(heap)  # Convert list into a heap
These are fundamental data structures, and understanding them is crucial for effective programming and algorithm design. Depending on your specific needs, you may choose different data structures for optimal performance.

## User
can you provide with their definitions and exampleS
Certainly! Let's go through the definitions and examples for each data structure:

## Lists:

Definition: An ordered collection of items. Mutable, meaning you can change the elements after the list is created.
Example:
python

## Tuples:

## Definition: Similar to lists but immutable. Once a tuple is created, you cannot change its elements.
Example:

my_tuple = (1, 2, 3, 'a', 'b')
## Sets:

Definition: An unordered collection of unique items. Mutable, meaning you can add or remove elements.
## Example:

my_set = {1, 2, 3, 'a', 'b'}
Dictionaries:

Definition: A collection of key-value pairs. Mutable and unordered.
Example:

my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
## Stacks:

Definition: Last In, First Out (LIFO) data structure. Elements are added and removed from the same end.
## Example:

stack = []
stack.append(1)
stack.append(2)
stack.pop()  # Removes and returns the last element (2)
## Queues:
Definition: First In, First Out (FIFO) data structure. Elements are added at the rear and removed from the front.
## Example:

from queue import Queue
my_queue = Queue()
my_queue.put(1)
my_queue.put(2)
my_queue.get()  # Removes and returns the first element (1)
## Linked Lists:

Definition: A collection of nodes, where each node contains data and a reference to the next node in the sequence.
Example:

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
## Trees:
-Definition: A hierarchical data structure with nodes connected by edges. Each node has a parent-child relationship.

## Example: Binary Tree

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
