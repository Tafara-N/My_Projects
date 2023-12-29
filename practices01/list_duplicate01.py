def duplicate_finder(list1, list2):
    list1 = set(list1)
    list2 = set(list2)
    new_list = list1.intersection(list2)
    return list(new_list)
def main():
    list1 = [2, 4, 7, 9, 5, 2]
    list2 = [3, 6, 2, 1, 9, 2]
    list3 = [1, 2, 3, 4, 5]
    list4 = [4, 5, 6, 7]
    result = duplicate_finder(list1, list2)
    result2 = duplicate_finder(list3, list4)
    result3 = duplicate_finder(list1, list3)
    result4 = duplicate_finder(list1, list4)
    result5 = duplicate_finder(list2, list4)
    print(result)
    print(result2)
    print(result3)
    print(result4)
    print(result5)

main()
