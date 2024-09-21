rivers = {
    "Nile": 6,650,
    "Amazon": 6,400,
    "Yangtze": 6,300,
    "Mississippi": 3,730,
    "Yellow River": 5,464,
    "Congo": 4,700
}

# Print the entire dictionary
print(rivers)

# Access and print the length of the 2nd river
print("Length of the 2nd river:", rivers["Amazon"])

# Update the length of the 5th river
rivers["Yellow River"] = 5464

# Delete the 4th river from the dictionary
del rivers["Mississippi"]

# Print the last key-value pair in the dictionary
last_river = list(rivers.items())[-1]
print("Last key-value pair:", last_river)
