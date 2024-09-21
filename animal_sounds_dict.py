animals = {
    "Cat": "Meow",
    "Dog": "Woof",
    "Cow": "Moo",
    "Horse": "Neigh",
    "Pig": "Oink",
    "Sheep": "Baah",
    "Duck": "Quack",
    "Rooster": "Cock-a-doodle-doo"
}

# Print the entire dictionary
print(animals)

# Access and print the sound of the 4th animal
print("Sound of the 4th animal:", animals["Horse"])

# Update the sound of the 7th animal
animals["Duck"] = "Quack quack"

# Delete the 5th animal from the dictionary
del animals["Pig"]

# Print the last key-value pair in the dictionary
last_animal = list(animals.items())[-1]
print("Last key-value pair:", last_animal)
