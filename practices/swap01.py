num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"Originally -> num1 = {num1}, num2 = {num2}")
num1, num2 = num2, num1
print(f"Swapped -> num1 = {num1}, num2 = {num2}")
