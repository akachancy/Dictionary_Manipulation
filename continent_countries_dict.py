continents = {
    "Asia": ["China", "India", "Japan"],
    "Africa": ["Egypt", "Nigeria", "South Africa"],
    "Europe": ["Germany", "France", "United Kingdom"],
    "North America": ["United States", "Canada", "Mexico"],
    "South America": ["Brazil", "Argentina", "Colombia"],
    "Australia": ["Australia", "New Zealand", "Papua New Guinea"]
}

# Print the entire dictionary
print(continents)

# Access and print the countries of the 4th continent
print("Countries of the 4th continent:", continents["North America"])

# Update the countries of the 5th continent
continents["South America"] = ["Brazil", "Argentina", "Peru"]

# Delete the 6th continent from the dictionary
del continents["Australia"]

# Print the last key-value pair in the dictionary
last_continent = list(continents.items())[-1]
print("Last key-value pair:", last_continent)