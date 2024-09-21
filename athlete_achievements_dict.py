athletes = {
    "Michael Jordan": "Winning six NBA championships with the Chicago Bulls",
    "Serena Williams": "Winning 23 Grand Slam singles titles in tennis",
    "Usain Bolt": "Breaking world records in the 100m, 200m, and 4x100m relay",
    "Lionel Messi": "Winning the FIFA World Cup with Argentina in 2022",
    "Tiger Woods": "Winning 15 major championships in golf",
    "Simone Biles": "Winning the most Olympic gold medals by an American female gymnast",
    "Roger Federer": "Winning 20 Grand Slam singles titles in tennis",
    "LeBron James": "Winning four NBA championships with three different teams"
}

# Print the entire dictionary
print(athletes)

# Access and print the achievement of the 5th athlete
print("Achievement of the 5th athlete:", athletes["Tiger Woods"])

# Update the achievement of the 3rd athlete
athletes["Usain Bolt"] = "Breaking world records in the 100m, 200m, and 4x100m relay, and winning eight Olympic gold medals"

# Delete the 7th athlete from the dictionary
del athletes["Roger Federer"]

# Print the last key-value pair in the dictionary
last_athlete = list(athletes.items())[-1]
print("Last key-value pair:", last_athlete)
