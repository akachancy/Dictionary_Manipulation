coffee_types = {
    "Espresso": "A strong, concentrated coffee made by forcing hot water through finely ground coffee beans.",
    "Latte": "A coffee drink made with espresso and steamed milk, often topped with a layer of foam.",
    "Cappuccino": "A coffee drink made with espresso, steamed milk, and foamed milk, often topped with cocoa powder or cinnamon.",
    "Americano": "A coffee drink made by adding hot water to espresso.",
    "Mocha": "A coffee drink made with espresso, chocolate syrup, and steamed milk.",
    "Macchiato": "A coffee drink made with espresso and a small amount of foam.",
    "Flat White": "A coffee drink made with espresso and steamed milk, with a thin layer of foam.",
    "Cortado": "A coffee drink made with espresso and steamed milk, in equal parts.",
    "Ristretto": "A smaller, more concentrated version of espresso.",
    "Affogato": "A coffee drink made with espresso poured over a scoop of ice cream."
}

# Print the entire dictionary
print(coffee_types)

# Access and print the description of the 4th type of coffee
print("Description of the 4th type of coffee:", coffee_types["Americano"])

# Update the description of the 8th type of coffee
coffee_types["Cortado"] = "A coffee drink made with espresso and steamed milk, in equal parts, often topped with a sprinkle of cinnamon."

# Delete the 5th type of coffee from the dictionary
del coffee_types["Mocha"]

# Print the last key-value pair in the dictionary
last_coffee_type = list(coffee_types.items())[-1]
print("Last key-value pair:", last_coffee_type)