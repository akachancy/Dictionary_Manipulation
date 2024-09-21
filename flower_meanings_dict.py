flowers = {
    "Rose": "Love, passion, beauty",
    "Lily": "Purity, innocence, rebirth",
    "Sunflower": "Happiness, loyalty, admiration",
    "Daisy": "Innocence, purity, cheerfulness",
    "Tulip": "Perfect love, spring, hope",
    "Orchid": "Luxury, beauty, strength",
    "Iris": "Wisdom, hope, faith",
    "Carnation": "Love, affection, admiration"
}

# Print the entire dictionary
print(flowers)

# Access and print the meaning of the 5th flower
print("Meaning of the 5th flower:", flowers["Tulip"])

# Update the meaning of the 7th flower
flowers["Iris"] = "Wisdom, faith, royalty"

# Delete the 6th flower from the dictionary
del flowers["Orchid"]

# Print the last key-value pair in the dictionary
last_flower = list(flowers.items())[-1]
print("Last key-value pair:", last_flower)
