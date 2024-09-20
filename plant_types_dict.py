plants = {
    "Oak": "Tree",
    "Rose": "Shrub",
    "Lavender": "Herb",
    "Sunflower": "Herb",
    "Cactus": "Succulent",
    "Fern": "Fern",
    "Bamboo": "Grass",
    "Orchid": "Epiphyte"
}

# Print the entire dictionary
print(plants)

# Access and print the type of the 5th plant
print("Type of the 5th plant:", plants["Cactus"])

# Update the type of the 2nd plant
plants["Rose"] = "Flowering shrub"

# Delete the 6th plant from the dictionary
del plants["Fern"]

# Print the last key-value pair in the dictionary
last_plant = list(plants.items())[-1]
print("Last key-value pair:", last_plant)