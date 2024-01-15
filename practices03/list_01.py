#!/usr/bin/python3

"""Listing elements"""

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

# Printing list_1 before extending it
print(list_1)

# Extending list_1 by list_2 using extend method and printing the extended list_1
list_1.extend(list_2)
print(list_1)

#Extending list 1 bylist 3 using the slicing method and print the extended list_1
list_1[len(list_1):] = list_3
print(list_1)

print(f"The number {7} appears {list_1.count(1)} time(s)")
