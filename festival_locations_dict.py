festivals = {
    "Oktoberfest": "Munich, Germany",
    "Carnival": "Rio de Janeiro, Brazil",
    "Coachella": "Indio, California, USA",
    "Burning Man": "Black Rock Desert, Nevada, USA",
    "Mardi Gras": "New Orleans, Louisiana, USA",
    "Bonnaroo": "Manchester, Tennessee, USA",
    "Tomorrowland": "Boom, Belgium",
    "Glastonbury Festival": "Pilton, England"
}

# Print the entire dictionary
print(festivals)

# Access and print the location of the 4th festival
print("Location of the 4th festival:", festivals["Burning Man"])

# Update the location of the 6th festival
festivals["Bonnaroo"] = "Manchester, Tennessee, USA"  # This is already correct

# Delete the 2nd festival from the dictionary
del festivals["Carnival"]

# Print the last key-value pair in the dictionary
last_festival = list(festivals.items())[-1]
print("Last key-value pair:", last_festival)
