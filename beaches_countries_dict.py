beaches = {
    "Waikiki Beach": "Hawaii, United States",
    "Copacabana Beach": "Rio de Janeiro, Brazil",
    "Bondi Beach": "Sydney, Australia",
    "Whitehaven Beach": "Queensland, Australia",
    "Grace Bay Beach": "Turks and Caicos Islands",
    "Playa del Carmen": "Mexico",
    "Palm Beach": "Florida, United States",
    "Cayo Coco": "Cuba"
}

# Print the entire dictionary
print(beaches)

# Access and print the country of the 3rd beach
print("Country of the 3rd beach:", beaches["Bondi Beach"])

# Update the country of the 6th beach
beaches["Playa del Carmen"] = "Mexico"  # This is already correct

# Delete the 5th beach from the dictionary
del beaches["Grace Bay Beach"]

# Print the last key-value pair in the dictionary
last_beach = list(beaches.items())[-1]
print("Last key-value pair:", last_beach)