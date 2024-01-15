#!/bin/python3

"""Finding the bigggest number"""

number = int(input("Enter the number of numbers you want: "))
number_list = []
for i in range(number):
    number_list.append(int(input(f"Enter number {i + 1}: ")))
max = number_list[1]
for i in number_list:
    if i > max:
        max = i
print(f"Your list: {number_list}")
print(f"Max number is: {max}")
