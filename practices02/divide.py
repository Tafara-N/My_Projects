number = int(input("Enter a number: "))
message = f"{number} is divisible by"
if number % 2 == 0 and number % 3 == 0:
    print(f"{message} both 2 & 3")
elif number % 2 == 0:
    print(f"{message} 2")
elif number % 3 == 0:
    print(f"{message} by 3")
else:
    print(f"{number} is not divisible by 2 or 3")
