sports_events = {
    "FIFA World Cup 2022": 2022,
    "Olympics 2024": 2024,
    "UEFA Euro 2024": 2024,
    "Wimbledon 2023": 2023,
    "US Open 2023": 2023,
    "Tour de France 2023": 2023,
    "NBA Finals 2023": 2023
}

# Print the entire dictionary
print(sports_events)

# Access and print the year of the 3rd sports event
print("Year of the 3rd sports event:", sports_events["UEFA Euro 2024"])

# Update the year of the 6th sports event
sports_events["Tour de France 2023"] = 2023  # This is already correct

# Delete the 5th sports event from the dictionary
del sports_events["US Open 2023"]

# Print the last key-value pair in the dictionary
last_sports_event = list(sports_events.items())[-1]
print("Last key-value pair:", last_sports_event)
