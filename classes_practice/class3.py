#!/usr/bin/python3
class Person :

    def __init__(self) :
        self.name = "Brendon"
        self.age = 19
        self.gender = "Male"

    def greeting(self) :
        print(f"Hello there, I'm {self.name}, aged {self.age} and I am {self.gender}")

    def vote(self) :
        if self.age >= 18 :
            print("I'm eligible to vote")
        else :
            print("I'm not eligible to vote")


my_object = Person()

my_object.greeting()
my_object.vote()
