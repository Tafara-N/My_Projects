#!/usr/bin/python3

#to get cuurent year
import datetime

# Ask for details
year_of_birth = input("Year of birth: ")
month_of_birth = input("Month of birth (0-12): ")
day_of_birth = input("Day of the month: ")

# current year
current_year = datetime.datetime.now().year

# Display details
print("Your date of birth is:", end=" ")
print(day_of_birth, month_of_birth, year_of_birth, sep="-")

# Calculate the age
age = current_year - int(year_of_birth)

# Display age
print("You are ", age, "years old.")
