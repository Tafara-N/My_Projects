#!/usr/bin/python3

myList = ["brendie", 21, 5.9]
names = ["given", "brendie", "not", "tanaka"]
nums = [4, 7, 1, 34, 10, 8]

# adding 20 to the end of the list
nums.append(20)
print(nums)

# adding multiple elements or a list to the list
nums.extend([21, 30, 45])
print(nums)

# reverse the list
nums.reverse()
print(nums)

# insert an item before 5
nums.insert(4, 25)
print(nums)

# insert at an index that does not exist
nums.insert(25, 18)
print(nums)

# insert at the beiginning
nums.insert(0, 18)
print(nums)

# sort and maintain
nums.sort()
print(nums)

# reverse with sort
nums.sort(reverse=True)
print(nums)

# for more
# print(help(nums))
