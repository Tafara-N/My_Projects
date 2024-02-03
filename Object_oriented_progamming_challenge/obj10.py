class Student:
    def __init__(self, name, house):
            self.name = name
            self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    ##Name Getter method
    @property
    def name(self):
        return (self._name)
    
    ## Name Setter method
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    ## House Getter Method
    @property
    def house(self):
        return (self._house)
    
    ## House Setter Method
    @house.setter
    def house(self, house):
        if house not in ["Sanwe", "Konut", "Mujuru", "Cherima"]:
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
