#!/usr/bin/python3

"""Sorting lists in ascending, descending and reverse order"""

list_1 = [12, 67, 89, 65, 45, 90, 63, 21, 12]
list_2 = [43, 61, 12, 89, 43, 67, 9, 17, 6, 81]
list_3 = [54, 26, 93, 6, 39, 72, 40, 89, 100]

# Sorting elements of list_1 using sort method
list_1.sort()
print(list_1)

# Sorting list_2 in reverse
list_2.sort(reverse=True)
print(list_2)

# Reverse the elements of list_3
list_3.reverse()
print(list_3)
