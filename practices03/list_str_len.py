#!/usr/bin/python3

# Question: Write a function that takes in a list of strings and returns a new list containing only the strings that have a length greater than 5.
def str_length(my_list):
    new_list = []
    for item in my_list:
        if len(item) > 5:
            new_list.append(item)
    return new_list
def main():
    list1 = ["Brendon", "The", "greatest", "manof", "Always", "handsome"]
    result = str_length(list1)
    print(result)
main()
