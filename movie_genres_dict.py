movies = {
    "Comedy": "The Big Sick",
    "Drama": "The Shawshank Redemption",
    "Sci-Fi": "Inception",
    "Action": "Mad Max: Fury Road",
    "Horror": "The Shining",
    "Animation": "Spirited Away",
    "Romance": "The Notebook",
    "Thriller": "Se7en"
}

# Print the entire dictionary
print(movies)

# Access and print the example movie of the 3rd genre
print("Example movie of the 3rd genre:", movies["Sci-Fi"])

# Update the example movie of the 5th genre
movies["Horror"] = "Halloween (2018)"

# Delete the 7th genre from the dictionary
del movies["Romance"]

# Print the last key-value pair in the dictionary
last_movie = list(movies.items())[-1]
print("Last key-value pair:", last_movie)
