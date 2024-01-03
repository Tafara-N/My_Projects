def greetings(**kwargs):
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end = " ")

greetings(title = "Mr.", first_name = "Brendon", midle_name = "Tendai", last_name = "Jeje")
print()
