technologies = {
    "Light bulb": "Thomas Edison",
    "Telephone": "Alexander Graham Bell",
    "Computer": "Alan Turing (conceptual), John von Neumann (practical)",
    "Internet": "Tim Berners-Lee",
    "Smartphone": "Martin Cooper",
    "Artificial Intelligence": "John McCarthy",
    "Electric Car": "Thomas Davenport",
    "Social Media": "David Recordon, Stewart Butterfield, and Jack Dorsey"
}

# Print the entire dictionary
print(technologies)

# Access and print the innovator of the 4th technology
print("Innovator of the 4th technology:", technologies["Internet"])

# Update the innovator of the 2nd technology
technologies["Telephone"] = "Alexander Graham Bell and Elisha Gray"

# Delete the 6th technology from the dictionary
del technologies["Artificial Intelligence"]

# Print the last key-value pair in the dictionary
last_technology = list(technologies.items())[-1]
print("Last key-value pair:", last_technology)