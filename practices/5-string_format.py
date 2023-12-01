#!/usr/bin/python3

fname = input("Firstname: ")
surname = input("Surname: ")
age = int(input("Age: "))

# Display details
# Using old style formatting
details = "Your name is %s %s and you are %d years old" %(fname, surname,age)
print(details)

print()
# Using the new style formatting (str.format{})
details = "Your name is {} {} and you are {} years old".format(fname, surname,age)
print(details)

print()
# Using specifiers in the new formatting style
details = "Your name is {:s} {:s} and you are {:d} years old".format(fname, surname,age)
print(details)

print()
# Using indices in the new formatting style
details = "Your name is {1} {0} and you are {2} years old".format(fname, surname,age)
print(details)

print()
# Using keywords in the new formatting style
details = "Your name is {fn} {ln} and you are {ag} years old".format(fn = fname, ln = surname, ag = age)
print(details)

print()
# Using the f-string formatting style
details = f"Your name is {fname} {surname} and you are {age} years old"
print(details)
# You can use the f-string to do a lot like operations
print(f"we have {3 + 3} examples so far")
