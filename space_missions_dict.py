space_missions = {
    "Apollo 11": 1969,
    "Voyager 1": 1977,
    "Hubble Space Telescope": 1990,
    "Mars Curiosity Rover": 2012,
    "James Webb Space Telescope": 2021
}

# Print the entire dictionary
print(space_missions)

# Access and print the year of the 3rd mission
print("Year of the 3rd mission:", space_missions["Hubble Space Telescope"])

# Update the year of the 2nd mission
space_missions["Voyager 1"] = 1977

# Delete the 4th mission from the dictionary
del space_missions["Mars Curiosity Rover"]

# Print the last key-value pair in the dictionary
last_mission = list(space_missions.items())[-1]
print("Last key-value pair:", last_mission)
