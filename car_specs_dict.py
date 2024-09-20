car_models = {
    "Toyota Camry": "2.5-liter inline-4",
    "Honda Accord": "2.0-liter turbocharged inline-4",
    "Tesla Model 3": "Electric motor",
    "Ford Mustang": "5.0-liter V8",
    "Nissan Leaf": "Electric motor",
    "Hyundai Sonata": "2.5-liter inline-4",
    "BMW 3 Series": "2.0-liter turbocharged inline-4",
    "Mercedes-Benz C-Class": "2.0-liter turbocharged inline-4",
    "Audi A4": "2.0-liter turbocharged inline-4",
    "Kia Optima": "2.5-liter inline-4"
}

# Print the entire dictionary
print(car_models)

# Access and print the specifications of the 4th car model
print("Specifications of the 4th car model:", car_models["Ford Mustang"])

# Update the specifications of the 9th car model
car_models["Audi A4"] = "2.0-liter turbocharged inline-4 (mild hybrid)"

# Delete the 5th car model from the dictionary
del car_models["Nissan Leaf"]

# Print the last key-value pair in the dictionary
last_car_model = list(car_models.items())[-1]
print("Last key-value pair:", last_car_model)