#!/usr/bin/python3

# Question: Given a list of integers, write a function to find the maximum and minimum values in the list and return them as a tuple.
"""Printing values in a tuple"""

def max_min_finder(list1):
    min = max = list1[0]
    for number in list1:
        if number > max:
            max = number
        elif number < min:
            min = number
    tuple1 = (min, max)
    return tuple1
def main():
    list1 = [24,7,12,2,9,45]
    result = max_min_finder(list1)
    print(result)

main()
