count = int(input("Enter the number of elements of your list: "))
list1 = []
for i in range(count):
    list_item = int(input(f"Enter item {i + 1}: "))
    list1.append(list_item)
print(list1)
