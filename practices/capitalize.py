str = "What ever the string is going to be capitalized"
str = str.split()
capitalized = ""
for word in str:
    capitalized = capitalized + " " + word.capitalize()
print(capitalized)
