cities = {
    "Tokyo": 37.39 million,
    "Delhi": 31.18 million,
    "Shanghai": 27.63 million,
    "São Paulo": 22.02 million,
    "Mexico City": 21.75 million,
    "Cairo": 20.48 million,
    "Beijing": 20.38 million,
    "Dhaka": 19.58 million,
    "Mumbai": 19.40 million,
    "Karachi": 15.70 million
}

# Print the entire dictionary
print(cities)

# Access and print the population of the 6th city
print("Population of the 6th city:", cities["Cairo"])

# Update the population of the 3rd city
cities["Shanghai"] = 28.00 million

# Delete the 9th city from the dictionary
del cities["Mumbai"]

# Print the last key-value pair in the dictionary
last_city = list(cities.items())[-1]
print("Last key-value pair:", last_city)