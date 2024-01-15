#!/usr/bin/python3

"""Checks if the number is divisible by 2 or not and results to True or False"""

# Write a function that finds all multiples of 2 in a list.
def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
def main():
    list1 = [1, 4, 8, 0, 9, 3, 1]
    new_list = divisible_by_2(list1)
    print(new_list)

main()
