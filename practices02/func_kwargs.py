# **kwargs -> parameter that will packs all the arguments into a dictionary

def greetings(**kwargs):
    print("Hello "+ kwargs["first_name"] + " " + kwargs["last_name"])

greetings(first_name = "Jace", last_name = "Jeje")
