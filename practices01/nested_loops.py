#Nested loops - The execution of loops inside of another loop
#              - The execution of inner loop finishes first before start executing outer loop

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
