#!/usr/bin/python3
import random

class Hat:

    houses = ["Murehwa", "Chinhoyi", "Gwanda", "Omalala"]

    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print("{} is in {}".format(name, house))

def main():
        
        Hat.sort("Jace")

if __name__ == "__main__":
     main()
