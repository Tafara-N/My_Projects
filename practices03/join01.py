#!/usr/bin/python3

# syntax -> seperator.join(iterable)

list1 = ['B', 'r', 'e', 'n', 'd', 'o', 'n']
# print(''.join(list1))
# print(' '.join(list1))
# print('_'.join(list1))

list2 = ["My", "name", "is", "Brendon"]
# print(" ".join(list2))

dictionary_01 = {"name": "Brendon", "age":19}
print(" and ".join(dictionary_01))

new_list = list1 + list2
print(new_list)
