historical_events = {
    "French Revolution": 1789,
    "American Civil War": 1861-1865,
    "Industrial Revolution": 1760-1840,
    "World War I": 1914-1918,
    "World War II": 1939-1945,
    "Cold War": 1947-1991,
    "Fall of the Berlin Wall": 1989,
    "Space Race": 1957-1975
}

# Print the entire dictionary
print(historical_events)

# Access and print the year of the 2nd event
print("Year of the 2nd event:", historical_events["American Civil War"])

# Update the year of the 7th event
historical_events["Fall of the Berlin Wall"] = 1989

# Delete the 5th event from the dictionary
del historical_events["World War II"]

# Print the last key-value pair in the dictionary
last_event = list(historical_events.items())[-1]
print("Last key-value pair:", last_event)
