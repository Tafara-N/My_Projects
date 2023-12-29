count = int(input("Enter number of list elements you want: "))
list2 = []
i = 0
while i < count:
    list_item = int(input(f"Enter element {i + 1}: "))
    list2.append(list_item)
    i = i + 1
print(list2)
