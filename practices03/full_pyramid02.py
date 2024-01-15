#!/usr/bin/python3

"""A pyramid using for loops"""

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for space in range(1, rows - i + 1):
        print(end=' ')
    for star in range(1, i + 1):
        print("*", end='')
    print('')
