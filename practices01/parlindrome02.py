input_str = input("Enter your string here: ")
right = len(input_str) - 1
left = 0
is_palindrome = True
while left < right:
    if input_str[left].lower() != input_str[right].lower():
        is_palindrome = False
        break
    right -= 1
    left += 1
if is_palindrome == True:
    print(f"{input_str} is a palindrome word")
else:
    print(f"{input_str} is not a palindrome word")
