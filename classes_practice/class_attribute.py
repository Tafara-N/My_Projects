#!/usr/bin/bash
class Person:
    
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    ...

person1 = Person("Rispo", 24)
person2 = Person()
person3 = Person()
person3.name = "Tashinga"
person3.age = 12

# print(Person)
# print(person1)
# print(person2)
# print(person3)

# print(Person.__doc__)

print(Person.__dict__)

print(person1.__dict__)
print(person2.__dict__)
print(person3.__dict__)

Person.name = "Dylan"
print(person1.name)
print(person2.name)
print(Person.name)
