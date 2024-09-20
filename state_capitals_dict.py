states_and_capitals = {
    "California": "Sacramento",
    "Texas": "Austin",
    "Florida": "Tallahassee",
    "New York": "Albany",
    "Illinois": "Springfield",
    "Pennsylvania": "Harrisburg",
    "Ohio": "Columbus",
    "Michigan": "Lansing",
    "Georgia": "Atlanta",
    "North Carolina": "Raleigh"
}

# Print the entire dictionary
print(states_and_capitals)

# Access and print the capital of the 4th state
print("Capital of the 4th state:", states_and_capitals["New York"])

# Update the capital of the 9th state
states_and_capitals["Georgia"] = "Atlanta"  # This is already correct

# Delete the 7th state from the dictionary
del states_and_capitals["Ohio"]

# Print the last key-value pair in the dictionary
last_state_capital = list(states_and_capitals.items())[-1]
print("Last key-value pair:", last_state_capital)