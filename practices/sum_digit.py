number = input("Enter the number here: ")
sum = 0
for digit in number:
    sum += int(digit)
print(f"The sum of digits in {number} is: {sum:d}")
