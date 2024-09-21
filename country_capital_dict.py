countries = {
    "United States": "Washington, D.C.",
    "Canada": "Ottawa",
    "China": "Beijing",
    "India": "New Delhi",
    "Brazil": "Brasília",
    "Russia": "Moscow",
    "Japan": "Tokyo",
    "Germany": "Berlin",
    "France": "Paris",
    "United Kingdom": "London",
    "South Africa": "Pretoria",
    "Australia": "Canberra"
}

# Print the entire dictionary
print(countries)

# Access and print the capital of the 5th country
print("Capital of the 5th country:", countries["Brazil"])

# Update the capital of the 8th country
countries["Germany"] = "Berlin (official), Bonn (de facto)"

# Delete the 11th country from the dictionary
del countries["South Africa"]

# Print the last key-value pair in the dictionary
last_country = list(countries.items())[-1]
print("Last key-value pair:", last_country)
