#!/usr/bin/python3
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        else:
            self.name = name
            self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    ## Getter
    @property
    def house(self):
        return (self._house)
    
    ## Setter
    @house.setter
    def house(self, house):
        if house not in ["St Adamsss", "Kariba", "Mujuru", "Los Angeles"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    # student.house = "Kondo"
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()
