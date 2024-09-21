recipes = {
    "Pizza": "Combine flour, water, yeast, and salt to make dough. Let it rise. Add pizza sauce, cheese, and toppings. Bake in a preheated oven.",
    "Spaghetti": "Cook spaghetti noodles. Combine tomato sauce, meat, and vegetables. Toss with cooked spaghetti.",
    "Chicken Alfredo": "Cook chicken. Make a creamy Alfredo sauce with butter, Parmesan cheese, and heavy cream. Combine chicken and sauce.",
    "Sushi": "Prepare sushi rice. Roll sushi with fillings like fish, vegetables, and seaweed. Cut into pieces.",
    "Tacos": "Warm tortillas. Fill with meat, cheese, lettuce, and salsa. Serve with lime wedges.",
    "Burger": "Grill a beef patty. Place on a bun with lettuce, tomato, cheese, and condiments.",
    "Fried Rice": "Cook rice. Sauté vegetables and meat. Combine with rice and add seasonings.",
    "Lasagna": "Cook lasagna noodles. Layer with ricotta cheese, meat sauce, and mozzarella cheese. Bake in a preheated oven."
}

# Print the entire dictionary
print(recipes)

# Access and print the recipe of the 5th food
print("Recipe for the 5th food:", recipes["Tacos"])

# Update the recipe of the 3rd food
recipes["Chicken Alfredo"] = "Cook chicken. Make a creamy Alfredo sauce with butter, Parmesan cheese, and milk. Combine chicken and sauce."

# Delete the 7th food from the dictionary
del recipes["Fried Rice"]

# Print the last key-value pair in the dictionary
last_recipe = list(recipes.items())[-1]
print("Last key-value pair:", last_recipe)
