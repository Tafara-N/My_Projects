def unique_list(my_list):
    traversed_list = []
    deleted = []
    for item in my_list:
        if item in deleted or item in traversed_list:
            deleted.append(item)
            traversed_list.remove(item)
        else:
            traversed_list.append(item)
    return traversed_list
def main():
    list1 = [1, 2, 3, 2, 4, 1, 5]
    result = unique_list(list1)
    print(result)

main()
