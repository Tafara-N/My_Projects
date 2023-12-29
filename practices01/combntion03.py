# Question: You are given two lists, list1 and list2, containing integers. Write a function to merge the two lists into a single sorted list in ascending order. You are not allowed to use any built-in sorting functions.

def combine_list(list1, list2):
    combined_list = list1 + list2
    n = len(combined_list)
    for i in range(n - 1):
        for j in range(n - i -1):
            if combined_list[j] > combined_list[j+1]:
                combined_list[j], combined_list[j+1] = combined_list[j+1], combined_list[j]
    return combined_list

def main():
    list1 = [1, 23, 13]
    list2 = [41, 56, 96]
    result = combine_list(list1, list2)
    print(result)

main()
