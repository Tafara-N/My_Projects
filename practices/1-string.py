#!/usr/bin/python3

for i in range(1,11):
    if i <= 5:
        print ("AAAAAAH" + ("H" * i) + "!")
        if i == 5:
            print()
    elif i >= 6 and i <=9:
        print ("WHERE ARE ALL THE BRACKETS!" + ("?" * i))
        if i == 9:
            print()
    else:
        print ("HOW DO YOU PEOPLE READ THIS SYNTAX EASILY? :(")
