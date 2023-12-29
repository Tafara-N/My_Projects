str = input("Enter the str here: ")
rev_str = str[::-1]
if str == rev_str:
    print(f"{str} is a palindrome word")
else:
    print(f"{str} is not a palindrome word")
