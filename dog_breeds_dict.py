dog_breeds = {
    "Chihuahua": "small",
    "Golden Retriever": "medium",
    "German Shepherd": "large",
    "Poodle": "medium",
    "Dachshund": "small",
    "Labrador Retriever": "large",
    "French Bulldog": "small",
    "Bulldog": "medium",
    "Beagle": "small",
    "Rottweiler": "large"
}

# Print the entire dictionary
print(dog_breeds)

# Access and print the size of the 5th breed
print("Size of the 5th breed:", dog_breeds["Dachshund"])

# Update the size of the 8th breed
dog_breeds["Bulldog"] = "medium"  # This is already correct

# Delete the 6th breed from the dictionary
del dog_breeds["Labrador Retriever"]

# Print the last key-value pair in the dictionary
last_breed = list(dog_breeds.items())[-1]
print("Last key-value pair:", last_breed)
