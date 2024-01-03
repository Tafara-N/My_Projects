my_string = "Brendon a.k.a 24hrP the greatest man. I like coding"
my_string = my_string.split()
for word in my_string[::-1]:
    if word == my_string[1]:
        print(word)
    else:
        print(word, end='..')
