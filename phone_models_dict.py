phone_models = {
    "iPhone 15 Pro Max": "Apple",
    "Samsung Galaxy S24 Ultra": "Samsung",
    "Google Pixel 8 Pro": "Google",
    "OnePlus 12": "OnePlus",
    "Xiaomi 14 Pro": "Xiaomi",
    "OPPO Find X7 Pro": "OPPO",
    "vivo X100 Pro": "vivo",
    "Motorola Edge 40 Pro": "Motorola",
    "Sony Xperia 5 V": "Sony",
    "Honor Magic6 Pro": "Honor"
}

# Print the entire dictionary
print(phone_models)

# Access and print the manufacturer of the 2nd phone model
print("Manufacturer of the 2nd phone model:", phone_models["Samsung Galaxy S24 Ultra"])

# Update the manufacturer of the 8th phone model
phone_models["Motorola Edge 40 Pro"] = "Motorola"  # This is already correct

# Delete the 6th phone model from the dictionary
del phone_models["OPPO Find X7 Pro"]

# Print the last key-value pair in the dictionary
last_phone_model = list(phone_models.items())[-1]
print("Last key-value pair:", last_phone_model)