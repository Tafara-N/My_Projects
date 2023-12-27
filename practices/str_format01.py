# str.format() - is an optional method available to string that gives the user more control when displaying the output

name = "Brendon"
nationality = "Zimbabwean"

#print("You are " + name + " and you are a " + nationality)
# print("You are {} and you are a {}".format("Brendon", "Zimbabwean"))
# print("You are {} and you are a {}".format(name, nationality))
# print("You are {0} and you are a {1}".format(name, nationality))
# print("You are a {1} and you are {0}".format(name, nationality))

text = "You are {} and you are a {}"
print(text.format(name, nationality))
