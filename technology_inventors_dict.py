technologies = {
    "Light bulb": "Thomas Edison",
    "Telephone": "Alexander Graham Bell",
    "Computer": "Alan Turing (conceptual), John von Neumann (practical)",
    "Internet": "Tim Berners-Lee",
    "Smartphone": "Martin Cooper",
    "Artificial Intelligence": "John McCarthy"
}

# Print the entire dictionary
print(technologies)

# Access and print the inventor of the 4th technology
print("Inventor of the 4th technology:", technologies["Internet"])

# Update the inventor of the 2nd technology
technologies["Telephone"] = "Alexander Graham Bell and Elisha Gray"

# Delete the 6th technology from the dictionary
del technologies["Artificial Intelligence"]

# Print the last key-value pair in the dictionary
last_technology = list(technologies.items())[-1]
print("Last key-value pair:", last_technology)
