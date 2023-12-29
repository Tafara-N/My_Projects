# Question: (Implement a function that takes in two lists of integers and 
            #returns a new list that contains the common elements between the two lists, without any duplicates.

def list_comparison(list1, list2):
    new_list = []
    for list1_item in list1:
        if list1_item in list2:
            new_list.append(list1_item)
    new_list = set(new_list)
    return new_list
def main():
    first_list = [67, 34, 51, 50, 80, 67]
    second_list = [54, 51, 33, 51, 80, 67]
    results = list_comparison(first_list, second_list)
    print(results)
main()
