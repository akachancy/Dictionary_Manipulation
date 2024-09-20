elements = {
    "Hydrogen": "H",
    "Helium": "He",
    "Lithium": "Li",
    "Carbon": "C",
    "Nitrogen": "N",
    "Oxygen": "O",
    "Fluorine": "F",
    "Neon": "Ne",
    "Sodium": "Na",
    "Magnesium": "Mg"
}

# Print the entire dictionary
print(elements)

# Access and print the symbol of the 6th element
print("Symbol of the 6th element:", elements["Oxygen"])

# Update the symbol of the 8th element
elements["Neon"] = "Ne"  # This element is already correct

# Delete the 9th element from the dictionary
del elements["Sodium"]

# Print the last key-value pair in the dictionary
last_element = list(elements.items())[-1]
print("Last key-value pair:", last_element)