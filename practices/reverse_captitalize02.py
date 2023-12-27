number = input("Enter the number here: ")

reversed_num = number[::-1]
number, reversed_num = int(number), int(reversed_num)
print(f"The reversed digits of {number:d} is: {reversed_num:d}")
