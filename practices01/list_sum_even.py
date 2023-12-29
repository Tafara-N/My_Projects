# Question: Given a list of numbers, write a function that returns the sum of all the even numbers in the list.
def sum_of_even(my_list):
    sum = 0
    for number in my_list:
        if number % 2 == 0:
            sum += number
    return sum

def main():
    list1 = [12, 23, 2, 7, 8]
    list2 = [2, 4, 6, 8, 3, 7, 2]
    result1 = sum_of_even(list1)
    result2 = sum_of_even(list2)
    print(result1, result2)
    
main()
