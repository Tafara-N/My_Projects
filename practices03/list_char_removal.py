#!/usr/bin/python3

#Write a function that removes all characters c and C from a string.
def no_c(my_string):
    for character in my_string:
        if character not in "Cc":
            print(character, end='')

def main():
   no_c("Best School")
   no_c("Chicago")
   no_c("C is fun!")

main()
