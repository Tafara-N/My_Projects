#!/usr/bin/python3
class Person :

    def __init__(self, name, gender, age) :
        self.name = name
        self.gender = gender
        self.age = age

    def greeting(self) :
        print(f"Hello there, I'm {self.name} and I am {self.age} years old")

    def vote(self) :
        if self.age >= 18 :
            print(f"I am eligible to vote")
        else :
            print("I'm not eligible to vote")

my_obj1 = Person("Tinashe", "Male", 13)
my_obj2 = Person("Precious", "female", 24)
my_obj3 = Person("Paidamoyo", "female", 31)
my_obj4 = Person("Mackenzie", "Male", 18)

my_obj1.greeting()
my_obj1.vote()

my_obj2.greeting()
my_obj2.vote()

my_obj3.greeting()
my_obj3.vote()

my_obj4.greeting()
my_obj4.vote()
