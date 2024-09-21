animals = {
    "Lion": "Africa",
    "Tiger": "Asia",
    "Elephant": "Africa and Asia",
    "Giraffe": "Africa",
    "Panda": "Asia",
    "Kangaroo": "Australia",
    "Polar Bear": "Arctic",
    "Monkey": "Africa, Asia, and South America"
}

# Print the entire dictionary
print(animals)

# Access and print the habitat of the 3rd animal
print("Habitat of the 3rd animal:", animals["Elephant"])

# Update the habitat of the 5th animal
animals["Panda"] = "China"

# Delete the 7th animal from the dictionary
del animals["Polar Bear"]

# Print the last key-value pair in the dictionary
last_animal = list(animals.items())[-1]
print("Last key-value pair:", last_animal)
