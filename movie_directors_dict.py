movies = {
    "The Godfather": "Francis Ford Coppola",
    "The Shawshank Redemption": "Frank Darabont",
    "The Dark Knight": "Christopher Nolan",
    "Pulp Fiction": "Quentin Tarantino",
    "12 Angry Men": "Sidney Lumet",
    "Schindler's List": "Steven Spielberg",
    "The Lord of the Rings: The Return of the King": "Peter Jackson",
    "Fight Club": "David Fincher",
    "Inception": "Christopher Nolan",
    "The Matrix": "Lana Wachowski and Lilly Wachowski"
}

# Print the entire dictionary
print(movies)

# Access and print the director of the 5th movie
print("Director of the 5th movie:", movies["12 Angry Men"])

# Update the director of the 9th movie
movies["Inception"] = "Christopher Nolan"

# Delete the 7th movie from the dictionary
del movies["The Lord of the Rings: The Return of the King"]

# Print the last key-value pair in the dictionary
last_movie = list(movies.items())[-1]
print("Last key-value pair:", last_movie)
