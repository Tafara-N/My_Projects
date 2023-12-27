str = "WhaTever You PUT here"
reversed_capitalization = ""
for char in str:
    if (char.isupper()):
        reversed_capitalization = reversed_capitalization + char.lower()
    else:
        reversed_capitalization = reversed_capitalization + char.upper()
print(reversed_capitalization)
