number = int(input("Enter the number: "))
reversed_num = 0;
while number != 0:
    remainder = number % 10
    reversed_num = (reversed_num * 10) + remainder
    number //= 10

print(f"The reversed digits is: {reversed_num}")
