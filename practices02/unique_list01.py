def unique_list(list):
    traversed_list = []
    for item in list:
        if item not in traversed_list:
            traversed_list.append(item)
    return traversed_list
def main():
    list1 = [1, 2, 3, 2, 4, 1, 5]
    result = unique_list(list1)
    print(result)

main()
