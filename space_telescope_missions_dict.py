space_telescopes = {
    "Hubble Space Telescope": "Observing the universe in visible, infrared, and ultraviolet light",
    "James Webb Space Telescope": "Observing the universe in infrared light",
    "Spitzer Space Telescope": "Observing the universe in infrared light",
    "Chandra X-ray Observatory": "Observing the universe in X-ray light",
    "Kepler Space Telescope": "Searching for exoplanets"
}

# Print the entire dictionary
print(space_telescopes)

# Access and print the mission of the 3rd telescope
print("Mission of the 3rd telescope:", space_telescopes["Spitzer Space Telescope"])

# Update the mission of the 1st telescope
space_telescopes["Hubble Space Telescope"] = "Observing the universe in visible, infrared, ultraviolet, and near-infrared light"

# Delete the 4th telescope from the dictionary
del space_telescopes["Chandra X-ray Observatory"]

# Print the last key-value pair in the dictionary
last_telescope = list(space_telescopes.items())[-1]
print("Last key-value pair:", last_telescope)