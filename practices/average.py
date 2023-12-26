# Write a program to find out the average of a set of integers
count = int(input("Enter the count of numbers you want to find the average for: "))
sum = 0
for number in range(count):
    num = int(input(f"Enter number {number + 1}: "))
    sum += num

average = sum / count
print(f"The average is: {average}")
