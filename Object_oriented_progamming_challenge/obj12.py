#!/usr/bin/python3
import random

class Hat:

    def __init__(self):
        self.houses = ["Vineelle", "Kaseke", "Mahangu", "Marvel"]

    def sort(self, name):
        house = random.choice(self.houses)
        print("{} is in {}".format(name, house))

def main():
    hat = Hat()
    hat.sort("Kelly")

if __name__ == "__main__":
    main()
