# Convert the following code into a list comprehension
animals = ["lion", "tiger", "monkey", "elephant", "frog"]
filtered_animals = []
for animal in animals:
    filtered_animals.append(animal.title())
print(filtered_animals)

# Solution
filtered_animals_solution = [animal1.title() for animal1 in animals]
print(filtered_animals_solution)
