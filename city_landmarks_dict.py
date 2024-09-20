cities_and_landmarks = {
    "Paris": "Eiffel Tower",
    "New York City": "Statue of Liberty",
    "Rome": "Colosseum",
    "Tokyo": "Tokyo Tower",
    "London": "Big Ben",
    "Sydney": "Sydney Opera House",
    "Rio de Janeiro": "Christ the Redeemer",
    "Dubai": "Burj Khalifa"
}

# Print the entire dictionary
print(cities_and_landmarks)

# Access and print the landmark of the 6th city
print("Landmark of the 6th city:", cities_and_landmarks["Sydney"])

# Update the landmark of the 2nd city
cities_and_landmarks["New York City"] = "Times Square"

# Delete the 7th city from the dictionary
del cities_and_landmarks["Rio de Janeiro"]

# Print the last key-value pair in the dictionary
last_city_and_landmark = list(cities_and_landmarks.items())[-1]
print("Last key-value pair:", last_city_and_landmark)