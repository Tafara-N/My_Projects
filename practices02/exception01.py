# exception - events detected during program execution that interrupts normal flow of  program

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(result)

except ZeroDivisionError as e:
    print(e)
    print("You can only devide with non zero digit")
except ValueError as e:
    print(e)
    print("You can only devide with a number")
except Exception as e:
    print(e)
    print("Something went wrong!")
