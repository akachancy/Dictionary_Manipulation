planets = {
    "Mercury": 57.9,
    "Venus": 108.2,
    "Earth": 149.6,
    "Mars": 227.9,
    "Jupiter": 778.6,
    "Saturn": 1426.7,
    "Uranus": 2870.9,
    "Neptune": 4498.1
}

# Print the entire dictionary
print(planets)

# Access and print the distance of the 3rd planet
print("Distance of the 3rd planet:", planets["Earth"])

# Update the distance of the 5th planet
planets["Jupiter"] = 778.6

# Delete the 7th planet from the dictionary
del planets["Uranus"]

# Print the last key-value pair in the dictionary
last_planet = list(planets.items())[-1]
print("Last key-value pair:", last_planet)