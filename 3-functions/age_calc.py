#!/usr/bin/python3

# name = "Brendon Jeje"
# age = 19

# Defining the function
def age_calc(name, yob, current_year): # parameters(placeholderss)
    age = current_year - yob
    print(f"{name}, you are {age} years old")

# Calling the function (positional arguments)
age_calc("Brendon", 2004, 2023) # arguments(values)
age_calc("Tinashe", 2007, 2023)

# Calling the function (keyword arguments)
age_calc(yob=2002, current_year=2023, name="Brendon")
