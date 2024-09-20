currencies = {
    "United States Dollar": "$",
    "Euro": "€",
    "British Pound": "£",
    "Japanese Yen": "¥",
    "Indian Rupee": "₹",
    "Chinese Yuan": "¥",
    "Australian Dollar": "$",
    "Canadian Dollar": "$",
    "South African Rand": "R",
    "Brazilian Real": "R$"
}

# Print the entire dictionary
print(currencies)

# Access and print the symbol of the 5th currency
print("Symbol of the 5th currency:", currencies["Indian Rupee"])

# Update the symbol of the 9th currency
currencies["South African Rand"] = "R"  # This is already correct

# Delete the 3rd currency from the dictionary
del currencies["British Pound"]

# Print the last key-value pair in the dictionary
last_currency = list(currencies.items())[-1]
print("Last key-value pair:", last_currency)