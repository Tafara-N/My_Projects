count = int(input("Enter number of elements: "))
numbers_list = input("Enter the list elements here: ").split()
for i in range(count):
    numbers_list[i] = int(numbers_list[i])
print(numbers_list)
