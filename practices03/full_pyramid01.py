# Question: Write a program to print the full pyramid of stars
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(0, rows - i):
        print(" ", end='')
    for k in range(1, i*2):
        if k % 2 != 0:
            print("*", end='')
        else:
            print(' ', end='')
    print('')
