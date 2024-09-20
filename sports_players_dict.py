sports = {
    "Basketball": "Michael Jordan",
    "Football": "Lionel Messi",
    "Tennis": "Roger Federer",
    "Cricket": "Sachin Tendulkar",
    "Baseball": "Babe Ruth",
    "Soccer": "Pelé",
    "Golf": "Tiger Woods",
    "Formula 1": "Lewis Hamilton",
    "Boxing": "Muhammad Ali",
    "Rugby": "Jonah Lomu"
}

# Print the entire dictionary
print(sports)

# Access and print the player of the 4th sport
print("Player of the 4th sport:", sports["Cricket"])

# Update the player of the 6th sport
sports["Soccer"] = "Cristiano Ronaldo"

# Delete the 10th sport from the dictionary
del sports["Rugby"]

# Print the last key-value pair in the dictionary
last_sport = list(sports.items())[-1]
print("Last key-value pair:", last_sport)