car_brands = {
    "Toyota": "Japan",
    "Ford": "United States",
    "Volkswagen": "Germany",
    "Honda": "Japan",
    "Hyundai": "South Korea",
    "Nissan": "Japan",
    "Chevrolet": "United States",
    "BMW": "Germany",
    "Mercedes-Benz": "Germany",
    "Kia": "South Korea"
}

# Print the entire dictionary
print(car_brands)

# Access and print the country of origin of the 3rd car brand
print("Country of origin of the 3rd car brand:", car_brands["Volkswagen"])

# Update the country of origin of the 7th car brand
car_brands["Chevrolet"] = "United States of America"

# Delete the 8th car brand from the dictionary
del car_brands["BMW"]

# Print the last key-value pair in the dictionary
last_car_brand = list(car_brands.items())[-1]
print("Last key-value pair:", last_car_brand)