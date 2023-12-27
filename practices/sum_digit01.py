number = int(input("Enter the number: "))
reversed_num = 0;
sum = 0
while number != 0:
    remainder = number % 10
    sum += remainder
    reversed_num = (reversed_num * 10) + remainder
    number //= 10

print(f"The sum of the digits of {reversed_num} is: {sum}")
