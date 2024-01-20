#!/usr/bin/python3
my_list = [1, 2, 3, 2, 1, 4, 5, 4]
item = 2
my_list = [x for x in my_list if x != item]
print (my_list)
