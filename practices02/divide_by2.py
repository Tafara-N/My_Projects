num = int(input("Enter your number here: "))
binary = bin(num)
if binary[-1] == '0':
    print(f"The number {num} is divisible by 2")
else:
    print(f"The number {num} is not divisible by 2")
