#!/usr/bin/python3

'''Generate the squares of a members of a list'''

nums = [1, 2, 3, 4]

# create an empty list as a container for squared numbers
sq_nums = []
# using a for loop 
for num in nums:
    sq_nums.append(num ** 2)

print(f"Before: {nums}")
print(f"After: {sq_nums}")

# using the list comprehension
