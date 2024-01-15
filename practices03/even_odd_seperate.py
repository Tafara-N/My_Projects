#!/usr/bin/python3

"""even or odd numbers"""

def seperate_even_odd(my_list):
    even_list = []
    odd_list = []
    for i in my_list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return even_list, odd_list
def main():
    list1 = [2,5,4,21,6,7]
    print(seperate_even_odd(list1))

main()
