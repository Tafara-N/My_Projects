# Question: Write a program to find the first and the last occurence of the letter 'o' and character ',' in "Hello, World".
str = "Hello, Worl"
first_occurance = str.find('o')
last_occurance = str.rfind('o')

print(f"The first occurance of 'o' is at index {first_occurance}")
print(f"The last occurance of 'o' is at index {last_occurance}")
