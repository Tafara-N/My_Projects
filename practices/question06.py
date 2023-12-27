# Question: Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is. For example, if your name is Robert Brett Roser, then the output should be R.B.Roser.

full_name = input("Enter your names: ")
names_list = full_name.split()
first_name, second_name, last_name = names_list[0][0], names_list[1][0], names_list[2]
print(f"{first_name}.{second_name}.{last_name}")
