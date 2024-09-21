fruits = {
    "Apple": "Red",
    "Banana": "Yellow",
    "Orange": "Orange",
    "Grape": "Purple",
    "Strawberry": "Red",
    "Pineapple": "Yellow",
    "Mango": "Yellow",
    "Blueberry": "Blue"
}

# Print the entire dictionary
print(fruits)

# Access and print the color of the 6th fruit
print("Color of the 6th fruit:", fruits["Pineapple"])

# Update the color of the 4th fruit
fruits["Grape"] = "Green"

# Delete the 7th fruit from the dictionary
del fruits["Mango"]

# Print the last key-value pair in the dictionary
last_fruit = list(fruits.items())[-1]
print("Last key-value pair:", last_fruit)
