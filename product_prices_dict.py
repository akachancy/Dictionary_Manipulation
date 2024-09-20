products = {
    "iPhone 14 Pro": 999,
    "Samsung Galaxy S23 Ultra": 1199,
    "Sony PlayStation 5": 499,
    "Nintendo Switch": 299,
    "MacBook Air M2": 1099,
    "Dell XPS 13": 899,
    "iPad Pro": 1099,
    "Apple Watch Series 8": 399,
    "AirPods Max": 549,
    "Samsung Galaxy Tab S9": 799
}

# Print the entire dictionary
print(products)

# Access and print the price of the 4th product
print("Price of the 4th product:", products["Nintendo Switch"])

# Update the price of the 9th product
products["AirPods Max"] = 549

# Delete the 6th product from the dictionary
del products["Dell XPS 13"]

# Print the last key-value pair in the dictionary
last_product = list(products.items())[-1]
print("Last key-value pair:", last_product)